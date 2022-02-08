const today = new Date();
// 月末だとずれる可能性があるため、1日固定で取得
var showDate = new Date(today.getFullYear(), today.getMonth(), today.getDate(), today.getDay());

// 初期表示
window.onload = function () {
    showProcess(today);
};
// 前の日表示
function prev(){
    showDate.setDate(showDate.getDate() - 1);
    showProcess(showDate);
}

function today_btn() {
    showProcess(today);
    showDate.setDate(today.getDate());
}

// 次の日表示
function next(){
    showDate.setDate(showDate.getDate() + 1);
    showProcess(showDate);
}

// 日付表示
function showProcess(date) {
    var year = date.getFullYear();
    var month = date.getMonth();
    var dates = date.getDate();
    var days = ["日","月","火","水","木","金","土"];
    var day = days[date.getDay()];
    document.querySelector('#header').innerHTML = year + "年 " + (month + 1) + "月" + dates + "日 " + day + "曜日";
    
}