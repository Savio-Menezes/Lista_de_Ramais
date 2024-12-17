function sortTable() {
    const table = document.getElementById('phoneDirectory');
    const rows = Array.from(table.rows).slice(1);
    const sortBy = document.getElementById('ordenar').value;

    const columnMap = {
        'ramal': 0,
        'usuario': 1,
        'setor': 3
    };

    rows.sort((a, b) => {
        const aText = a.cells[columnMap[sortBy]].innerText.toLowerCase();
        const bText = b.cells[columnMap[sortBy]].innerText.toLowerCase();

        return aText.localeCompare(bText);
    });

    rows.forEach(row => table.tBodies[0].appendChild(row));
}
