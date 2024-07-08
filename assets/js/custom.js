function filter_table() {
    let input = document.getElementById("search_field");
    let filter = input.value.toUpperCase();
    let table = document.getElementById("device_table");

    for (let row of table.rows) {
        if (row.className == "header") { continue; }
        row.style.display = "none";
        for (let cell of row.cells) {
            if (cell.textContent.toUpperCase().includes(filter)) {
                row.style.display = "";
            }
        }
    }
}