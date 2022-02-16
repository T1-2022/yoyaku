const week = ["(日)", "(月)", "(火)", "(水)", "(木)", "(金)", "(土)"];
const today = new Date();
var showDate = new Date(today.getFullYear(), today.getMonth(), 1);
var startDay = "";
let reserves = [];

// 初期表示
window.onload = function () {
    current();
    calendar_week_ajax();
};

// 前の週へ
function prev() {
    startDay = changeDate(startDay, -7);
    //createCalendar();
}

// 今の週へ
function current() {
    var year = today.getFullYear();
    var month = today.getMonth() + 1;
    var date = today.getDate();
    var currentDay = year + "/" + month + "/" + date;
    startDay = changeDate(currentDay, -today.getDay());
    //createCalendar();
}

// 次の週へ
function next() {
    startDay = changeDate(startDay, 7);
    //createCalendar();
}

// カレンダー作成
function createCalendar() {
    var start = startDay.split("/");
    var year = Number(start[0]);
    var month = Number(start[1]);
    var date = Number(start[2]);

    var calendar = "<table class='table table-bordered'>";
    calendar += createDate();
    calendar += createReserve();
    calendar += "</table>";

    document.querySelector('#date').innerHTML = year + "年 " + month + "月" + date + "日～";
    document.querySelector('#calendar').innerHTML = calendar;
}

// カレンダー日にち部分作成
function createDate() {
    var calendar = "<thead><tr><th scope='col'>　</th>";

    for (var i = 0; i < week.length; i++) {
        // 日加算
        var day = changeDate(startDay, i).split("/");
        var year = Number(day[0]);
        var month = Number(day[1]);
        var date = Number(day[2]);

        // 曜日
        if (today.getFullYear() == year
            && today.getMonth() == month - 1
            && today.getDate() == date) calendar += "<th scope='col' class='table-primary'>";
        else if (i == 0) calendar += "<th scope='col' class='sunday'>";
        else if (i == 6) calendar += "<th scope='col' class='saturday'>";
        else calendar += "<th scope='col'>";

        // 変数代入
        calendar += month + "/" + date + week[i] + "</th>";
    }
    calendar += "</tr><thead>";

    return calendar;
}

// カレンダー予約部分作成
function createReserve() {
    var calendar = "<tbody>";

    for (var i = 0; i < conferences.length; i++) {
        calendar += "<tr><th scope='row'>" + conferences[i] + "</th>";
        for (var j = 0; j < week.length; j++) {
            // 日加算
            var day = changeDate(startDay, j).split("/");
            var year = Number(day[0]);
            var month = Number(day[1]);
            var date = Number(day[2]);

            // 予約検索
            calendar += "<td>";
            for (k = 0; k < reserves.length; k++) {
                var reserveDay = reserves[k][4].split("/");
                if (i == reserves[k][2] - 1
                    && year == Number(reserveDay[0])
                    && month == Number(reserveDay[1])
                    && date == Number(reserveDay[2])) {

                    // ボタン内容定義
                    var id = reserves[k][0];
                    var time = reserves[k][5] + "~" + reserves[k][6]
                    var text = time + "<br>" + reserves[k][7];

                    // 予約詳細定義
                    var detail = "　　　　　　予約者名　　：" + reserves[k][3] + "<br>";
                    detail += "　　　　　　予約時間　　：" + time + "<br>";
                    detail += "　　　　　　　目的　　　：" + reserves[k][9] + "<br>";
                    detail += "　　　　　　利用者名　　：" + reserves[k][7] + "<br>";
                    detail += "　　　　　利用者連絡先　：" + reserves[k][8] + "<br>";
                    detail += "　　　　　　　備考　　　：" + reserves[k][10];

                    // 削除できるかチェック
                    var delete_button = "";
                    if (adminFlag == true || reserves[k][11] == registerID) {
                        delete_button = "<button class='btn btn-secondary' type='submit' data-bs-dismiss='modal'>削除</button>";
                    }

                    // ボタン設定
                    calendar += "<button class='btn btn-secondary font-small' type='button' data-bs-toggle='modal' data-bs-target='#reserve" + id + "' ";
                    calendar += "onclick = 'setReserve(" + id + ")'>" + text + "</button>";
                    calendar += "<div class='modal fade' id='reserve";
                    calendar += reserves[k][0] + "' tabindex=' - 1' aria-hidden='true'>";
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
                    calendar += "   <form name='reserveForm' method='post'>"
                    calendar += "       <input hidden type='text'  name='reserveID' id='reserveID" + id + "'>";
                    calendar +=         delete_button;
                    calendar += "   </form>";
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
    calendar += "</tbody>";

    return calendar;
}

// 日にち変更計算
function changeDate(day, num) {
    day = day.split("/");
    var year = Number(day[0]);
    var month = Number(day[1]);
    var date = Number(day[2]);
    var endDate = new Date(year, month, 0).getDate();

    date += num;
    if (date > endDate) {
        month = month % 12 + 1;
        date = date % endDate;
        if (month == 1) year++;
    }
    if (date < 1) {
        month = (month + 10) % 12 + 1;
        date = new Date(year, month, 0).getDate() + date;
        if (month == 12) year--;
    }

    var result = year + "/" + month + "/" + date;
    return result;
}

// 予約内容取得
function setReserve(num) {
    var formName = "reserveID" + num;
    document.querySelector('input[id="' + formName + '"]').value = num;
}

function calendar_week_ajax(){
    calendar_ajax_POST(startDay);
    calendar_ajax_GET();
}

function calendar_ajax_GET() {
    //window.alert('GET開始');
    $(function () {
        $.ajax({
            type: "GET",
            url: "/main/week_Ajax_GET",
            dataType: "json",
        })
            .done(function (data) {
                reserves = data;
                createCalendar();
            })
            //通信失敗時の処理
            .fail(function () {
                window.alert('データが取れていません');
                createCalendar();
            })
    })


}

function calendar_ajax_POST(data) {
    json = JSON.stringify(data);  // object型からJSON文字列(string型)に変換

    $.ajax({
        type: "POST",
        url: "/main/week_Ajax_POST",
        data: json,
        contentType: "application/json",
        success: function (msg) {
            console.log(msg);
        },
        error: function (msg) {
            console.log("error");
        }
    })
    //window.alert('POST完了');
}
