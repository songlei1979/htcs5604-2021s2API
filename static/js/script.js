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

function addAnOutlet(OutletName, Streetaddress, Suburb, City, Postcode, ContactFirstName, ContactLastName, Emailaddress, PhoneNumber){
    var msg = "";
    $.ajax({
            type: 'POST',
            url: 'https://htcs5604-2021s2api.herokuapp.com/addanoutletAPI',
            async: false,
            dataType: "JSON", // data type expected from server
            data: JSON.stringify({
                OutletName: OutletName,
                Streetaddress: Streetaddress,
                Suburb: Suburb,
                City: City,
                Postcode: Postcode,
                ContactFirstName: ContactFirstName,
                ContactLastName: ContactLastName,
                Emailaddress: Emailaddress,
                PhoneNumber: PhoneNumber,
            }),
            success: function (data) {
                msg = data;
            },
            error: function(err) {
                msg= err;
            }
        });
    return msg;
}