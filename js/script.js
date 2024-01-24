$(document).ready(function(){
    // Default sort for QS Ranking
    var defaultSortIndex = $('th').filter(function() {
        return $(this).text() === 'QS Ranking';
    }).index();

    sortTable(defaultSortIndex, true);

    $('th').click(function(){
        var index = $(this).index();
        var asc = $(this).hasClass('asc');
        sortTable(index, !asc);
    });

    function sortTable(index, asc) {
        var table = $('table');
        var rows = table.find('tr:gt(0)').toArray().sort(comparer(index, asc));

        if (!asc){
            rows = rows.reverse();
            $('th').eq(index).removeClass('asc').addClass('desc');
        } else {
            $('th').eq(index).removeClass('desc').addClass('asc');
        }

        $('th').not($('th').eq(index)).removeClass('asc').removeClass('desc');

        for (var i = 0; i < rows.length; i++){table.append(rows[i]);}
    }

    function comparer(index, asc) {
        return function(a, b) {
            var valA = convertRank(getCellValue(a, index));
            var valB = convertRank(getCellValue(b, index));
            return valA - valB;
        };
    }

    function convertRank(value) {
        if (value.includes('-')) {
            var parts = value.split('-').map(Number);
            return parts[0];
        }
        return parseFloat(value) || Number.MAX_SAFE_INTEGER;
    }

    function getCellValue(row, index){
        return $(row).children('td').eq(index).html();
    }

    $('#searchbox').keyup(function() {
        var searchTerm = $(this).val().toLowerCase();
        $('#universitiesTable tbody tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(searchTerm) > -1)
        });
    });
});
