const total_sales = document.querySelector(".total_sales")
const customers_visited = document.querySelector(".customers_visited")
const average_sales = document.querySelector(".average_spending")
const table = document.querySelector(".tableDiv")
const login = document.querySelector("form")
const page = document.querySelector(".form-container")
const dashboard = document.querySelector(".retail-dashboard")



login.addEventListener('submit', e => {
    // prevents default action
    e.preventDefault();

    // get the username and password
    const username = login.username.value.trim();
    const password = login.password.value.trim();
    login.reset();



    authenticate(username, password).then(Response => {
        // console.log(Response.access_token);
        window.localStorage.setItem('token', Response.access_token);

    });

    if (window.localStorage.getItem('token') !== "undefined") {
        // page.innerHTML = "<a href='./index.html'>click here to enter RAGE-FASHION</a>";
        page.style.display = "none";
        dashboard.style.display = "block";



        getDailySales(window.localStorage.getItem('token'))
            .then(response => {
                console.log(response.items)
                let li = `<tr><td>USER-ID</td><td>PRODUCT-ID</td><td>SALE-AMOUNT</td><td>SALE-DATE</td></tr>`;
                response.items.forEach(user => {
                    li += `<tr><td>${user.user_id}</td><td>${user.product_id}</td><td>${user.sale_amount}</td><td>${user.sale_date}</td>`
                })
                table.innerHTML = li
            })
            .catch(err => console.log(err));

        getTotalSales(window.localStorage.getItem('token'))
            .then(data => {
                total_sales.textContent = data["total sales"]
                console.log(data["total sales"])
            })
            .catch(err => console.log(err))

        getUniqueCustomers(window.localStorage.getItem('token'))
            .then(response => {
                customers_visited.textContent = response.unique_visitors
                console.log(response.unique_viitors)
            })
            .catch(err => console.log(err));



        getAverageSales(window.localStorage.getItem('token'))
            .then(response => {
                average_sales.textContent = response["average sales per customer"]
                console.log(response["average sales per customer"])
            }
            )
            .catch(err => console.log(err));



    }
    else {
        page.innerHTML = "<a href=#>INVALID CREDENTIALS</a>"

    }

});