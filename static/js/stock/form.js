var produ = {
    items:{
        products:[]
    },
    add: function(item){
        this.items.products.push(item);
        this.list();
    }, 
    list: function () {
        $('#datain').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                {"data": "descripcion"},
                {"data": "cantidad"},
                {"data": "date"},
                {"data": "nro_remito"},
                {"data": "nro_rq"},
                {"data": "observacion"},
            ],
            columnDefs: [
                {
                    targets: [1,2,3,4,5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm" autocomplete="off" >';
                    }
                },
             
            ],
            initComplete: function (settings, json) {

            }
        });
    },  
};

$(function () {
    // Buscar Producto
    $("#search").autocomplete({
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
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.log(produ.items);
            produ.add(ui.item);
            $(this).val('');
        }

    });

});