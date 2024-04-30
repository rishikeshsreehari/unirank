$(document).ready(function(){
    // Default sort for QS Ranking
    var defaultSortIndex = $('th[data-sort="qs"]').index();

    sortTable(defaultSortIndex, true);
    $('th').eq(defaultSortIndex).addClass('asc'); // Add 'asc' class to the default sorted column header

    $('th:not(:first-child)').click(function(){ // Only bind click event to non-first th elements
        var index = $(this).index();
        var asc = !$(this).hasClass('asc'); // Toggle sorting order

        sortTable(index, asc);

        // Remove sorting icons from all headers
        $('th').removeClass('asc desc');
        // Add sorting icon class to clicked header
        $(this).addClass(asc ? 'asc' : 'desc');
    });

    function sortTable(index, asc) {
        var table = $('table');
        var rows = table.find('tr:gt(0)').toArray().sort(comparer(index, asc));

        // Update the table with sorted rows
        for (var i = 0; i < rows.length; i++) {
            table.append(rows[i]);
        }
    }

    function comparer(index, asc) {
        return function(a, b) {
            var valA = convertRank(getCellValue(a, index));
            var valB = convertRank(getCellValue(b, index));
            return asc ? valA - valB : valB - valA; // Adjust sorting order based on 'asc' flag
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
        return $(row).children('td').eq(index).text(); // Change .html() to .text() to get text content
    }

    $('#searchbox').keyup(function() {
        var searchTerm = $(this).val().toLowerCase();
        $('#universitiesTable tbody tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(searchTerm) > -1)
        });
    });
});



// Function to toggle between dark and light modes
function toggleDarkLightMode() {
    var stylesheet = document.getElementById("stylesheet");
    var lightIcon = document.getElementById("light-icon");
    var darkIcon = document.getElementById("dark-icon");

    if (stylesheet.getAttribute("href") === "css/styles-dark.css") {
        stylesheet.setAttribute("href", "css/styles-light.css");
        lightIcon.style.display = "none";
        darkIcon.style.display = "inline-block";
    } else {
        stylesheet.setAttribute("href", "css/styles-dark.css");
        lightIcon.style.display = "inline-block";
        darkIcon.style.display = "none";
    }
}

// Add a click event listener to the mode toggle icon
document.getElementById("dark-light-toggle").addEventListener("click", toggleDarkLightMode);

// Initially, set the dark button to be shown since light mode is active by default
var darkIcon = document.getElementById("dark-icon");
darkIcon.style.display = "inline-block";