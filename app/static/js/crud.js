"use strict";
/**
 * @fileoverview Code in crud.js handles crud functionality for the frontend served to the client.
 * Uses the FetchAPI to send requests to the backend.
 * @package
 */

// Constants
// Set the server host and server ports
/** The IP address or hostname of the server */
const serverHost = "127.0.0.1";
/** The Port number of the server */
const serverPort = 8000;
/** the base url structure of server requests */
const baseUrl = "http://" + serverHost + ":" + serverPort;


/**
 * Sends a request to get all of the clients from the database
 * @returns All Clients in JSON format
 */
function getAllClients() {
    return fetch(baseUrl + "/clients/").then((Response) => { return Response.json() });
}

/**
 * Sends a request to get all of the vehicles from the database
 * @returns All Vehicles in JSON format
 */
function getAllVehicles() {
    return fetch(baseUrl + "/vehicles/").then((Response) => { return Response.json() });
}

/**
 * Sends a request to get a particular client based on client_id
 * @param {*} client_id UUID of the client
 * @returns The client in JSON format
 */
function getClientById(client_id = "") {
    return fetch(baseUrl + "/clients/" + client_id).then((Response) => { return Response.json() });
}

/**
 * Get the client_name attribute of a client
 * 
 * @param {*} client_id UUID of the client
 * @returns String containing the client name
 */
function getClientName(client_id = "") {
    /** String with the request to the specific backend route */
    const response = fetch(baseUrl + "/clients/" + client_id, {
        method: 'GET',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'omit',
        headers: {
            'Content-Type': 'application/json'
        },
    });

    /** String containing the client name or the placeholder */
    let clientCoolName = "client name";

    // Process the response promise to get the client's name
    clientCoolName = response.then((Response) => { 
        return Response.json(); 
    }).then((client_data) => {
        let clientName = client_data.client_name;
        clientCoolName = clientName;
        return clientName;
    });

    return clientCoolName;
}

/**
 * Sends a POST request to the backend to create a new client
 * @param {*} client JSON data 
 * @returns JSON response
 */
function createClient(client = {}) {
    /** Contains the route the backend is expecting */
    const response = fetch(baseUrl + "/clients/", {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'omit',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(client),
    });

    return response.then((Response) => { return Response.json() });
}

/**
 * Sends a PATCH request to the backend to update a client
 * @param {*} client_id UUID of the client to be updated
 * @param {*} client JSON data of the client with or without updated fields
 * @returns JSON response
 */
function updateClient(client_id = "", client = {}) {
    /** Contains the route that the backend is expecting */
    const response = fetch(baseUrl + "/clients/" + client_id, {
        method: 'PATCH',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'omit',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(client),
    });

    return response.then((Response) => { return Response.json() });
}

/**
 * Sends a DELETE request to delete a client
 * @param {*} client_id UUID of client to be deleted
 * @returns JSON response
 */
function deleteClient(client_id = "") {
    /** Contains the route that the backend is expecting */
    const response = fetch(baseUrl + "/clients/" + client_id, {
        method: 'DELETE', 
        mode: 'cors', 
        cache: 'no-cache', 
        credentials: 'omit',
        headers: {
            'Content-Type': 'application/json'
        },
    });

    return response.then((Response) => { return Response.json() }); 
}

/**
 * Sends a POST request to create a vehicle for a specific client
 * @param {*} client_id UUID of the vehicle's owner
 * @param {*} vehicle JSON data of the vehicle
 * @returns JSON response
 */
function createVehicle(client_id = "", vehicle = {}) {
    /** Contains the route the backend is expecting */
    const response = fetch(baseUrl + "/clients/" + client_id + "/vehicles", {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'omit',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(vehicle),
    });

    return response.then((Response) => { return Response.json() });
}

/**
 * Sends a DELETE request to delete a vehicle
 * @param {*} vehicle_id UUID of the vehicle
 * @returns JSON response
 */
function deleteVehicle(vehicle_id = "") {
    /** Contains the route the backend is expecting */
    const response = fetch(baseUrl + "/vehicles/" + vehicle_id, {
        method: 'DELETE', 
        mode: 'cors', 
        cache: 'no-cache', 
        credentials: 'omit',
        headers: {
            'Content-Type': 'application/json'
        },
    });

    return response.then((Response) => { return Response.json() }); 
}