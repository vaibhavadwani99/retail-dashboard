// post: user registration
const registration = async () => {

    const base = 'http://127.0.0.1:5000/register';

    const response = await fetch(base,
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username: "vaibhav", password: "abc" })
        });
    const data = await response.json();

    // return data;
    return data;
};
registration()
    .then(response => response.message)
    .then(json => console.log(json))
    .catch(err => console.log("Error fetching the data", err))


// post: user authentication

const authenticate = async (username, password) => {

    const base = 'http://127.0.0.1:5000/auth';
    username = username;
    password = password;



    const response = await fetch(base, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: username, password: password })
    });
    const data = await response.json();

    return data;

};


//GET- daily sales data

const getDailySales = async (token) => {


    const base = 'http://127.0.0.1:5000/sales';

    const response = await fetch(base, {
        method: 'GET',
        headers: {
            "Authorization": `JWT ${token}`
        }
    });

    const data = await response.json();

    return data;

};


// GET- total_sales

const getTotalSales = async (token) => {

    const base = 'http://127.0.0.1:5000/total_sales/21-02-2022';

    const response = await fetch(base, {
        method: 'GET',
        headers: {
            "Authorization": `JWT ${token}`
        }
    });

    const data = await response.json();

    return data;

};


// GET unique visitors 

const getUniqueCustomers = async (token) => {

    const base = 'http://127.0.0.1:5000/unique_visitors/21-02-2022';

    const response = await fetch(base, {
        method: 'GET',
        headers: {
            "Authorization": `JWT ${token}`
        }
    });

    const data = await response.json();

    return data;

};


// GET average sales per customer

const getAverageSales = async (token) => {

    const base = 'http://127.0.0.1:5000/average_sales/21-02-2022';

    const response = await fetch(base, {
        method: 'GET',
        headers: {
            "Authorization": `JWT ${token}`
        }
    });

    const data = await response.json();

    return data;

};