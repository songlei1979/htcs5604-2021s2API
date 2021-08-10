function viewAllProduct(){
    var products = []
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/products',
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                products = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return products;
}

function viewOneProduct(ProductID){
    var product = "";
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/product/'+ProductID,
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                product = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return product;
}

function productCategory(categoryID){
    var category = "";
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/productcategory/'+categoryID,
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                category = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return category;
}

function productsByCategory(categoryID){
    var products = "";
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/productsByCategory/'+categoryID,
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                products = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return products;
}

function productCategories(){
    var categories = "";
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/productcategories',
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                categories = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return categories;
}

function viewAllOtulets(){
    var outlets = []
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/outlets',
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                outlets = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return outlets;
}

function viewAnOutlet(OutletID){
    var outlet = "";
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/outlet/'+OutletID,
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                outlet = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return outlet;
}

function addAnOutlet(inputdata){

    $.ajax({
            type: 'POST',
            url: 'https://htcs5604-2021s2api.herokuapp.com/addanoutletAPI',
            dataType: "JSON", // data type expected from server
            async:false,
            data: inputdata,
            success: function (data) {
                msg = data;
            },
            error: function(err) {
                msg= err;
            }
        });
    var msg = "New outlet saved successfully";
    return msg;
}

function addAProduct(inputdata){

    $.ajax({
            type: 'POST',
            url: 'https://htcs5604-2021s2api.herokuapp.com/addaproductAPI',
            dataType: "JSON", // data type expected from server
            async:false,
            data: inputdata,
            success: function (data) {
                msg = data;
            },
            error: function(err) {
                msg= err;
            }
        });
    var msg = "New product saved successfully";
    return msg;
}

function viewOrdersByMonthAndYear(month, year){
    http://127.0.0.1:5000/completedOrdersByMonth/?month=8&year=2021
    var orders = []
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/completedOrdersByMonth/?month='+month+'&year='+year,
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                orders = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return orders;
}

function getTotalPriceForAnOrder(OrderNumber){
    var total = 0;
    $.ajax({
            type: 'GET',
            url: 'https://htcs5604-2021s2api.herokuapp.com/orderTotalPrice/'+OrderNumber,
            async: false,
            dataType: "JSON", // data type expected from server
            success: function (data) {
                total = data;
            },
            error: function(err) {
                console.log('Error: ' + err);
            }
        });
    return total;
}
