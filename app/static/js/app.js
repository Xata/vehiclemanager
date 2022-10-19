"use strict";
/**
 * @fileoverview The code in app.js handles all of the functionality of root webpage of VehicleManager.
 * 
 * @package
 */

// Constants
/** Initializes Bootstrap Tooltips. Selects them by the data-bs-toggle attribute */ 
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
/** Part of Bootstrap Tooltip Initialization. Put all elements with data-bs-toggle attribute in a list */ 
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// Define Document Elements
/** Table body where clients are displayed */
const $tableBodyClients = document.getElementById("tbody-clients");
/** Table body where vehicles are displayed */
const $tableBodyVehicles = document.getElementById("tbody-vehicles");

/** Button for creating a new client */
const $createNewClient = document.getElementById("create-new-client-submit-btn");

/** Button for editing an existing client */
const $editExistingClient = document.getElementById("edit-client-btn");

/** Button for deleting an existing client */
const $deleteExistingClient = document.getElementById("delete-client-btn");

/** Button for creating a new vehicle */
const $createNewVehicle = document.getElementById("create-new-vehicle-submit-btn");

/** Button for deleting a new vehicle */
const $deleteExistingVehicle = document.getElementById("delete-vehicle-btn");

// Define Bootstrap Icon HTML code
/** HTML for the "add" icon across the web app */
const addIconHTML = "<button type='button' id='add-icon-btn' class='btn btn-secondary'><i class='bi bi-plus-square-fill'></i></button>";

/** HTML for the "edit" icon across the web app */
const editIconHTML = "<button type='button' id='edit-icon-btn' class='btn btn-warning'><i class='bi bi-pencil-square'></i></button>";

/** HTML for the "trash" icon across the web app */
const trashIconHTML = "<button type='button' id='trash-icon-btn' class='btn btn-danger'><i class='bi bi-trash'></i></button>";

// Define Bootstrap Modals
/** Modal for the edit client functionality */
const $editClientModal = new bootstrap.Modal(document.getElementById("edit-client-modal"), { keyboard: false});

/** Modal for the delete client functionality */
const $deleteClientModal = new bootstrap.Modal(document.getElementById("delete-client-modal"), { keyboard: false});

/** Modal for the create new vehicle functionality */
const $createNewVehicleModal = new bootstrap.Modal(document.getElementById("create-new-vehicle-modal"), { keyboard: false});

/** Modal for the delete vehicle functionality */
const $deleteVehicleModal = new bootstrap.Modal(document.getElementById("delete-vehicle-modal"), { keyboard: false});
 

// Define Table Rows
/** Stores the rows from the Client table body */
let $clientRows;

/** Stores the rows from the Vehicle table body */
let $vehicleRows;

/**
 * Contains app functionality that is reused
 */
function app() {
    // Refresh the tables in index.html
    refreshTable();
}

/**
 * Refreshes tables in index.html
 * Sends a request to the backend to get the current database information
 */
function refreshTable() {
    // Get all the clients and put them in rows
    getAllClients().then((clients) => { $clientRows = clientHandler(clients); });

    // Get all the vehicles and put them in rows
    getAllVehicles().then((vehicles) => { $vehicleRows = vehicleHandler(vehicles); });
}

/**
 * Handles vehicle data from backend to display in a table
 * 
 * @param {*} data - Takes in Vehicle data from the backend
 * @returns HTMLTableRowElement
 */
function vehicleHandler(data) {
    return data.map((vehicle, i) => makeVehicleRow(vehicle, i));

    /**
     * Creates and Updates a row containing vehicle data
     * 
     * @param {*} vehicle  Vehicle data in JSON format
     * @param {*} i  Index. This is the current count index
     * @returns $vehicleTableRow - HTMLTableRowElement
     */
    async function makeVehicleRow(vehicle, i) {
        // Define variables for function
        /** Create new table row element */
        let $vehicleTableRow = document.createElement('tr');
        /** Create a div to contain the action button toolbar */
        let $buttonToolbar = document.createElement('div');
        /** Create a div to contain the button group for the delete button */
        let $deleteButtonGroup = document.createElement('div');
        /** Get the vehicle owner's name from the UUID */
        let vehicleOwnerDisplayName = await getClientName(vehicle.vehicle_owner_id);

        // Set the attributes for the button toolbar that contains the action buttons
        $buttonToolbar.setAttribute("class", "btn-toolbar");
        $buttonToolbar.setAttribute("role", "toolbar");
        $buttonToolbar.setAttribute("aria-label", "Action Button Toolbar");

        // Set the attributes for the button group that contains the delete button
        $deleteButtonGroup.setAttribute("class", "btn-group me-3");
        $deleteButtonGroup.setAttribute("role", "group");
        $deleteButtonGroup.setAttribute("aria-label", "Delete Button Group");

        // Apply the data from the database to the row
        $vehicleTableRow.innerHTML = `<td>${vehicle.vehicle_year}</td><td>${vehicle.vehicle_make}</td><td>${vehicle.vehicle_model}</td><td>${vehicleOwnerDisplayName}</td>`;

        // Delete Icon functionality
        /** Create a td (table data cell) */
        let $tdVehicleDelete = document.createElement('td');
        
        // Set the inside of the tag to be the trash icon
        $tdVehicleDelete.innerHTML = trashIconHTML;

        /**
         * Handle click event for the delete button
         */
        $tdVehicleDelete.onclick = function () {
            // Toggle the delete vehicle modal on
            $deleteVehicleModal.toggle();

            /**
             * Handle click event for the delete modal
             */
            $deleteExistingVehicle.onclick = function () {
                // Actually delete the vehicle from the database
                deleteVehicle(vehicle.vehicle_id).then(function () { location.reload()});
            }
        }

        // Add the created elements to the table row
        $deleteButtonGroup.append($tdVehicleDelete);
        $buttonToolbar.append($deleteButtonGroup);
        $vehicleTableRow.appendChild($buttonToolbar);

        $tableBodyVehicles.appendChild($vehicleTableRow);

        // Return the table row
        return $vehicleTableRow;
    }
}

/**
 * Handles client data from backend to display in a table
 * 
 * @param {*} data Client data in JSON format
 * @returns HTMLTableRowElement
 */
function clientHandler(data) {
    return data.map((client, i) => makeClientRow(client, i));

    /**
     * Creates and Updates a row containing client data
     * 
     * @param {*} client Client data in JSON format
     * @param {*} i Index. This is the current count index
     * @returns HTMLTableRowElement
     */
    function makeClientRow(client, i) {
        /** Create new table row element */
        let $clientTableRow = document.createElement('tr');
        /** Div element for the button toolbar */
        let $buttonToolbar = document.createElement('div');
        /** Div element containing the add button */
        let $addButtonGroup = document.createElement('div');
        /** Div element containing the edit button */
        let $editButtonGroup = document.createElement('div');
        /** Div element containing the delete button */
        let $deleteButtonGroup = document.createElement('div');

        // Set the attributes for the button toolbar that contains the action buttons
        $buttonToolbar.setAttribute("class", "btn-toolbar");
        $buttonToolbar.setAttribute("role", "toolbar");
        $buttonToolbar.setAttribute("aria-label", "Action Button Toolbar");

        // Set Individual Button Group attributes
        // Set the attributes for the button group that contains the add button
        $addButtonGroup.setAttribute("class", "btn-group");
        $addButtonGroup.setAttribute("role", "group");
        $addButtonGroup.setAttribute("aria-label", "Add Button Group");

        // Set the attributes for the button group that contains the edit button
        $editButtonGroup.setAttribute("class", "btn-group me-3");
        $editButtonGroup.setAttribute("role", "group");
        $editButtonGroup.setAttribute("aria-label", "Edit Button Group");

        // Set the attributes for the button group that contains the delete button
        $deleteButtonGroup.setAttribute("class", "btn-group me-3");
        $deleteButtonGroup.setAttribute("role", "group");
        $deleteButtonGroup.setAttribute("aria-label", "Delete Button Group");

        // New Client button functionality
        /**
         * Handle click event for creating a new client
         */
        $createNewClient.onclick = function () {
            // Send POST request to backend 
            createClient({
                client_name: document.getElementById("create-new-client-name-field").value,
                client_email: document.getElementById("create-new-client-email-field").value,
                client_phone: document.getElementById("create-new-client-phone-field").value
            }).then(function () {
                // Get any database updates
                refreshTable();

                // Reload the webpage
                location.reload();
            });
        }

        // Edit Icon functionality
        /** Div element containing the edit button */
        let $tdEdit = document.createElement('div');
        // Set the icon for the button
        $tdEdit.innerHTML = editIconHTML;

        /**
         * Handle click events for the edit button
         */
        $tdEdit.onclick = function () {
            /** Stores the name field from the edit client modal */
            let $editNameField = document.getElementById("edit-client-name-field")
            /** Stores the email field from the edit client modal */
            let $editEmailField = document.getElementById("edit-client-email-field")
            /** Stores the phone field from the edit client modal */
            let $editPhoneField = document.getElementById("edit-client-phone-field")

            // Set the attributes of the modal
            // Apply the current data to the fields so that we can send a complete response
            $editNameField.setAttribute("placeholder", client.client_name);
            $editEmailField.setAttribute("placeholder", client.client_email);
            $editPhoneField.setAttribute("placeholder", client.client_phone);
            $editNameField.setAttribute("value", client.client_name);
            $editEmailField.setAttribute("value", client.client_email);
            $editPhoneField.setAttribute("value", client.client_phone);

            // Turn on the edit client modal
            $editClientModal.toggle();

            /**
             * Handle the click event for the button in the modal
             */
            $editExistingClient.onclick = function () {
                // Send the PATCH request to the backend
                updateClient(client.client_id, {
                    client_name: $editNameField.value,
                    client_email: $editEmailField.value,
                    client_phone: $editPhoneField.value
                }).then(function () {
                    location.reload();
                });
            }
        }

        // Delete icon functionality
        /** Div element containing the delete button */
        let $tdDelete = document.createElement('div');
        
        // Set the icon for the delete button
        $tdDelete.innerHTML = trashIconHTML;

        /**
         * Handle the click events for the delete button
         */
        $tdDelete.onclick = function () {
            // Turn on the modal to prompt deletion confirmation
            $deleteClientModal.toggle()
            /**
             * Handle the click event for the confirm button
             */
            $deleteExistingClient.onclick = function () {
                // Send DELETE request to the backend
                deleteClient(client.client_id).then(location.reload());
            }
        }

        // Add icon functionality
        /** Div element containing the add button */
        let $tdAddVehicle = document.createElement('div');
        
        // Set the icon of the add button
        $tdAddVehicle.innerHTML = addIconHTML;

        /**
         * Handle click events for the add button
         */
        $tdAddVehicle.onclick = function () {
            // Get the element fields from the modal
            /** Year field */
            let $newVehicleYearField = document.getElementById("new-vehicle-year-field");
            /** Make field */
            let $newVehicleMakeField = document.getElementById("new-vehicle-make-field");
            /** Model field */
            let $newVehicleModelField = document.getElementById("new-vehicle-model-field");
            /** Current mileage field */
            let $newVehicleMileageField = document.getElementById("new-vehicle-mileage-field");
            /** Owner field */
            let $newVehicleOwnerField = document.getElementById("new-vehicle-owner-field");

            // Get the client UUID
            let client_UUID = client.client_id;

            // Toggle the modal
            $createNewVehicleModal.toggle();

            // Set the owner field
            // This has to pass the UUID later when we interact with the database
            $newVehicleOwnerField.setAttribute("value", client.client_name);

            /**
             * Handle the click event on the submit button
             */
            $createNewVehicle.onclick = function () {
                // Send the POST request to the backend
                createVehicle(client_UUID, {
                    vehicle_year: parseInt($newVehicleYearField.value),
                    vehicle_make: $newVehicleMakeField.value,
                    vehicle_model: $newVehicleModelField.value,
                    vehicle_mileage: parseInt($newVehicleMileageField.value)
                }).then(function () {
                    location.reload();
                });
            }
            
        }

        // Set the cells in the row to reflect the data from the database
        $clientTableRow.innerHTML = `<th scope="row">${i + 1}</th><td>${client.client_name}</td><td>${client.client_email}</td><td>${client.client_phone}</td>`;

        // Append the created buttons to respective group
        $addButtonGroup.append($tdAddVehicle);
        $editButtonGroup.append($tdEdit);
        $deleteButtonGroup.append($tdDelete);

        // Append the buttons in order
        $buttonToolbar.append($editButtonGroup);
        $buttonToolbar.append($deleteButtonGroup);
        $buttonToolbar.append($addButtonGroup);

        // Append the button toolbar to the row
        $clientTableRow.appendChild($buttonToolbar);

        // Append the row to the rest of the table
        $tableBodyClients.appendChild($clientTableRow);

        return $clientTableRow;
    }

}

// Run the app script
// Call the app function
app();
