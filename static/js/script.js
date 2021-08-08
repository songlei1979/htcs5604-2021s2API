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