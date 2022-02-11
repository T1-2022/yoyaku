var optionLoop, this_day, this_month, this_year, today;
today = new Date();
this_year = today.getFullYear();
this_month = today.getMonth() + 1;
this_day = today.getDate();
max_year = 5

// Listboxの作成
function createListBox(start, end, id, def) {
    var i, opt;

    opt = null;
    for (i = start; i <= end; i++) {
        if (i === def) {
            opt += "<option value='" + i + "' selected>" + i + "</option>";
        } else {
            opt += "<option value='" + i + "'>" + i + "</option>";
        }
    }
    return document.getElementById(id).innerHTML = opt;
};

createListBox(this_year, this_year + max_year, 'select_year', this_year);
createListBox(1, 12, 'select_month', this_month);
createListBox(1, 31, 'select_day', this_day);
createListBox(0, 23, 'select_start_hour', 0);
createListBox(0, 59, 'select_start_minute', 0);
createListBox(0, 23, 'select_end_hour', 0);
createListBox(0, 59, 'select_end_minute', 0);
createListBox(this_year, this_year + max_year, 'regular_year', this_year);
createListBox(1, 12, 'regular_month', this_month);
createListBox(1, 31, 'regular_day', this_day);
