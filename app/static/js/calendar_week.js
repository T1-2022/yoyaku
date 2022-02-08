const week = ["(日)", "(月)", "(火)", "(水)", "(木)", "(金)", "(土)"];
const today = new Date();
var showDate = new Date(today.getFullYear(), today.getMonth(), 1);
var numberWeek = 0; // 一ヶ月の週数
var currentWeek = 1; // 当月の何週目か
var todayWeek = 0;
var rateOther = 100; // 先月、翌月の日に乗算

// 仮予約データ
let yoyaku = [
    // id, user_id, conf_id, date, time, user_name, user_email, purpose, remarks
    [0, 0, 0, "2020/2/10", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 0, "2020/2/10", "14:00-16:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 1, "2020/2/11", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 2, "2020/2/9", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 3, "2020/2/11", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"],
    [0, 0, 4, "2020/2/11", "10:00-12:00", "○○先生", "test@email.com", "利用目的", "備考"]
];

// 初期表示
window.onload = function () {
    showProcess(today, calendar);
    currentWeek = todayWeek;
    showProcess(today, calendar);
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
    document.querySelector('#date').innerHTML = year + "年 " + (month + 1) + "月";
}

// カレンダー作成
function createProcess(year, month) {
    var dataMonth = createCalendar(year, month);
    var calendar = "<table><tr class='dayOfWeek'>";

    // 日付
    calendar += "<th>" + " " + "</th>";
    for (var i = 0; i < week.length; i++) {
        // 今日
        if (today.getFullYear() == year
            && today.getMonth() == month
            && today.getDate() == dataMonth[currentWeek - 1][i]) {
            calendar += "<th class='today'>" + (month + 1) + "/" + dataMonth[currentWeek - 1][i];
        }
        else {
            // 曜日
            if (i == 0) calendar += "<th class='sunday'>";
            else if (i == 6) calendar += "<th class='saturday'>";
            else calendar += "<th>";

            // 先月
            if (dataMonth[currentWeek - 1][i] >= rateOther * 10) {
                calendar += ((month + 11) % 12 + 1) + "/" + dataMonth[currentWeek - 1][i] / rateOther;
            }
            // 翌月
            else if (dataMonth[currentWeek - 1][i] >= rateOther) {
                calendar += ((month + 1) % 12 + 1) + "/" + dataMonth[currentWeek - 1][i] / rateOther;
            }
            // 当月
            else {
                calendar += (month + 1) + "/" + dataMonth[currentWeek - 1][i];
            }
        }
        calendar += week[i] + "</th>";
    }
    calendar += "</tr>";

    // 予約情報
    for (var i = 0; i < 6; i++) {
        calendar += "<tr><td>" + "会議室" + (i + 1)  + "</td>";
        for (var j = 0; j < week.length; j++) {
            // 日付計算
            if (dataMonth[currentWeek - 1][j] >= rateOther * 10) {
                var currentMonth = (month + 11) % 12 + 1;
                var currentDate = dataMonth[currentWeek - 1][j] / rateOther;
            } else if (dataMonth[currentWeek - 1][j] >= rateOther) {
                var currentMonth = (month + 1) % 12 + 1;
                var currentDate = dataMonth[currentWeek - 1][j] / rateOther;
            } else {
                var currentMonth = month + 1;
                var currentDate = dataMonth[currentWeek - 1][j];
            }

            // 予約検索
            calendar += "<td>";
            for (k = 0; k < yoyaku.length; k++) {
                var date = yoyaku[k][3].split("/");
                if (i == yoyaku[k][2]
                    && currentMonth == Number(date[1])
                    && currentDate == Number(date[2])) {
                    var text = yoyaku[k][4] + "<br>" + yoyaku[k][5];

                    //var detail = "　予約者名　：";// + yoyaku[k][0] + "\n";
                    //detail += "　予約時間　：" + yoyaku[k][4] + "\n";
                    //detail += "　　目的　　：" + yoyaku[k][7] + "\n";
                    //detail += "　利用者名　：" + yoyaku[k][5] + "\n";
                    //detail += "利用者連絡先：" + yoyaku[k][6] + "\n";
                    //detail += "　　備考　　：" + yoyaku[k][8];

                    calendar += "<button class='reserve' type='button'>" + text + "</button>";
                    //calendar += "<button class='reserve' type='button' onClick='confirm(" + detail + ");'>" + text + "</button>";
                }
            }
            calendar += "</td>";
        }
        calendar += "</tr>";
    }

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
