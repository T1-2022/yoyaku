const week = ["(日)", "(月)", "(火)", "(水)", "(木)", "(金)", "(土)"];
const today = new Date();
var showDate = new Date(today.getFullYear(), today.getMonth(), 1);
var numberWeek = 0; // 一ヶ月の週数
var currentWeek = 1; // 当月の何週目か
var todayWeek = 1;
var rateOther = 100; // 先月、翌月の日に乗算
var startDay = ""; //HTMLに送信する最初の日付

// 仮予約データ
let yoyaku = [
    // id, user_id, conf_id, date, time, user_name, user_email, purpose, remarks
    [0, 0, 0, "2022/2/10", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 0, "2022/2/10", "14:00-16:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 1, "2022/2/11", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 2, "2022/2/9", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 3, "2022/2/11", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 4, "2022/2/11", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"]
];

// 初期表示
window.onload = function () {
    showProcess(showDate);
};

// 前の週へ
function prev() {
    currentWeek--;
    if (currentWeek < 1) {
        currentWeek = 0;
        showDate.setMonth(showDate.getMonth() - 1);
    }
    showProcess(showDate);
}

// 今の週へ
function current() {
    currentWeek = todayWeek;
    showDate.setYear(today.getFullYear());
    showDate.setMonth(today.getMonth());
    showProcess(showDate);
}

// 次の週へ
function next() {
    currentWeek++;
    if (currentWeek > numberWeek) {
        currentWeek = 9;
        showDate.setMonth(showDate.getMonth() + 1);
    }
    showProcess(showDate);
}

// カレンダー表示
function showProcess(date) {
    var year = date.getFullYear();
    var month = date.getMonth();
    var calendar = createProcess(year, month);
    
    document.querySelector('#calendar').innerHTML = calendar;
    document.querySelector('#date').innerHTML = year + "年 " + (month + 1) + "月" + todayWeek + "/" + currentWeek;
    document.querySelector('#start_day').innerHTML = startDay;
}

// カレンダー作成
function createProcess(year, month) {
    var dataMonth = createCalendar(year, month);
    var calendar = "<table class='table table-bordered'>";
    var arrayYear = [];
    var arrayMonth = [];
    var arrayDay = [];

    // 日付
    calendar += "<thead><tr><th scope='col'>　</th>";
    for (var i = 0; i < week.length; i++) {
        // 曜日
        if (today.getFullYear() == year
            && today.getMonth() == month
            && today.getDate() == dataMonth[currentWeek - 1][i]) calendar += "<th scope='col' class='table-primary'>"
        else if (i == 0) calendar += "<th scope='col' class='sunday'>";
        else if (i == 6) calendar += "<th scope='col' class='saturday'>";
        else calendar += "<th scope='col'>";

        // 先月
        if (dataMonth[currentWeek - 1][i] >= rateOther * 10) {
            if (month + 1 == 1) var Y = year - 1;
            else Y = year;
            var M = ((month + 11) % 12 + 1);
            var D = dataMonth[currentWeek - 1][i] / rateOther;
        }
        // 翌月
        else if (dataMonth[currentWeek - 1][i] >= rateOther) {
            if (month + 1 == 12) var Y = year + 1;
            else Y = year;
            var M = ((month + 1) % 12 + 1);
            var D = dataMonth[currentWeek - 1][i] / rateOther;
        }
        // 当月
        else {
            var Y = year;
            var M = (month + 1);
            var D = dataMonth[currentWeek - 1][i];
        }

        // 変数代入
        arrayYear.push(Y);
        arrayMonth.push(M);
        arrayDay.push(D);
        calendar += M + "/" + D + week[i] + "</th>";

        // HTMLに送る日付設定
        if (i == 0) startDay = Y + "/" + M + "/" + D;
    }
    calendar += "</tr></thead>";

    // 予約情報
    calendar += "<tbody>";
    for (var i = 0; i < 6; i++) {
        calendar += "<tr><th scope='row'>" + "会議室" + (i + 1)  + "</th>";
        for (var j = 0; j < week.length; j++) {
            // 予約検索
            calendar += "<td>";
            for (k = 0; k < yoyaku.length; k++) {
                var date = yoyaku[k][3].split("/");
                if (i == yoyaku[k][2]
                    && arrayYear[j] == Number(date[0])
                    && arrayMonth[j] == Number(date[1])
                    && arrayDay[j] == Number(date[2])) {

                    // ボタン内容定義
                    var text = yoyaku[k][4] + "<br>" + yoyaku[k][5];

                    // 予約詳細定義
                    var detail = "　　　　　　予約者名　　：" + yoyaku[k][0] + "<br>";
                    detail +=    "　　　　　　予約時間　　：" + yoyaku[k][4] + "<br>";
                    detail +=    "　　　　　　　目的　　　：" + yoyaku[k][7] + "<br>";
                    detail +=    "　　　　　　利用者名　　：" + yoyaku[k][5] + "<br>";
                    detail +=    "　　　　　利用者連絡先　：" + yoyaku[k][6] + "<br>";
                    detail +=    "　　　　　　　備考　　　：" + yoyaku[k][8];

                    // ボタン設定
                    calendar += "<button class='btn btn-secondary font-small' type='button' data-bs-toggle='modal' data-bs-target='#test'>" + text + "</button>";
                    calendar += "<div class='modal fade' id='test' tabindex='-1' aria-hidden='true'>";
                    calendar += "<div class='modal-dialog'>";
                    calendar += "<div class='modal-content'>";

                    // ポップアップ中身
                    calendar += "<div class='modal-header'>";
                    calendar += "   <h5 class='modal-title'>予約詳細</h5>";
                    calendar += "   <button class='btn-close' type='button' data-bs-dismiss='modal' aria-label='Close'></button>";
                    calendar += "</div>";
                    calendar += "<div class='modal-body'>";
                    calendar += "   <p class='text-left'>" + detail + "</p>";
                    calendar += "</div>";
                    calendar += "<div class='modal-footer'>";
                    calendar += "   <button class='btn btn-secondary' type='button' data-bs-dismiss='modal'>変更</button>";
                    calendar += "   <button class='btn btn-secondary' type='button' data-bs-dismiss='modal'>削除</button>";
                    calendar += "</div>";

                    calendar += "</div>";
                    calendar += "</div>";
                    calendar += "</div>";
                    calendar += "</div>";
                }
            }
            calendar += "</td>";
        }
        calendar += "</tr>";
    }
    calendar += "</tbody></table>";

    return calendar;
}

// 一ヶ月カレンダー作成
function createCalendar(year, month) {
    var startDayOfWeek = new Date(year, month, 1).getDay();
    var endDate = new Date(year, month + 1, 0).getDate();
    var lastMonthEndDate = new Date(year, month, 0).getDate();
    var row = Math.ceil((startDayOfWeek + endDate) / week.length);
    var count = 0;
    var overlapFlag = 0;
    var dataMonth = [];
    var dataWeek = [];

    // 日付計算
    for (var i = 0; i < row; i++) {
        dataWeek = [];
        for (var j = 0; j < week.length; j++) {
            // 先月
            if (i == 0 && j < startDayOfWeek) {
                dataWeek.push((lastMonthEndDate - startDayOfWeek + j + 1) * rateOther);
                overlapFlag = overlapFlag | 1;
            }
            // 翌月
            else if (count >= endDate) {
                count++;
                dataWeek.push((count - endDate) * rateOther);
                overlapFlag = overlapFlag | 2;
            }
            // 当月
            else {
                count++;
                dataWeek.push(count);
                if (today.getFullYear() == year
                    && today.getMonth() == month
                    && today.getDate() == count) {
                    todayWeek = i + 1;
                }
            }
        }
        dataMonth.push(dataWeek);
    }

    // 月変化時の週番号計算
    numberWeek = row;
    if (currentWeek == 0) {
        currentWeek = numberWeek - (overlapFlag & 2) / 2;
    }
    if (currentWeek == 9) {
        currentWeek = 1 + (overlapFlag & 1);
    }

    return dataMonth;
}
