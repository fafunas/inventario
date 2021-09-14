$(function () {
    // Buscar Producto

    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            })
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            console.log("hi")
        }
    });
});