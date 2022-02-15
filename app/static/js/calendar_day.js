const today = new Date();
// 月末だとずれる可能性があるため、1日固定で取得
var showDate = new Date(today.getFullYear(), today.getMonth(), today.getDate(), today.getDay());
var day_disp = "";

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
    var calendar = createProcess(year, month, dates);

    document.querySelector('#calendar').innerHTML = calendar;
    document.querySelector('#header').innerHTML = year + "年 " + (month + 1) + "月" + dates + "日 " + day + "曜日";
    day_disp = year + "年 " + (month + 1) + "月" + dates + "日 " + day + "曜日";
}

// カレンダー作成
function createProcess(year, month, dates) {
    //var dataMonth = createCalendar(year, month);
    var calendar = "<table><tr class='OneDay'>";
    var use_time = ["08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30"];
    //var room_name = ["会議室1","会議室2","会議室3","会議室4","会議室5","会議室6","会議室7","会議室8"];

    // 日付
    calendar += "<tr><th></th>";
    for (var i = 0; i < use_time.length; i++) {
        calendar += "<th>" + use_time[i] + "</th>";
    }
    calendar += "</tr>";
    for (var j = 0; j < room.length; j++) {
        calendar += "<tr><th scope='row'>" + room[j] + "</th>";
        for (var k = 0; k < use_time.length; k++) {
            // 予約検索
            calendar += "<td>";
            for (var l = 0; l < yoyaku.length; l++) {
                //dateを年月日に分割
                var date = yoyaku[l][3].split("/");
                //時間を取得
                var start_time = yoyaku[l][4];
                var end_time = yoyaku[l][5];
                //使用時間の計算
                var st_t_h = yoyaku[l][4].split(":");
                var en_t_m = yoyaku[l][5].split(":");
                var use_st = Number(st_t_h[0]);
                var use_en = Number(en_t_m[0]);
                //スタート時間を数字にする
                if ( Number(st_t_h[1]) == 15 ){
                    use_st += 0.25;
                }
                else if ( Number(st_t_h[1]) == 30 ) {
                    use_st += 0.5;
                }
                else if ( Number(st_t_h[1]) == 45 ) {
                    use_st += 0.75;
                }
                else {
                    use_st += 0;
                }
                //エンド時間を数字にする
                if ( Number(en_t_m[1]) == 15 ){use_en += 0.25;}
                else if ( Number(en_t_m[1]) == 30 ) {use_en += 0.5;}
                else if ( Number(en_t_m[1]) == 45 ) {use_en += 0.75;}
                else {use_en += 0;}
                //使用時間
                var using = use_en - use_st;

                if ( Number(date[0]) == year
                    && Number(date[1]) == month+1
                    && Number(date[2]) == dates
                    && room[j] == yoyaku[l][2]
                    && use_time[k] == yoyaku[l][4]){


                    // ボタン内容定義
                    var text = yoyaku[l][4] + "-" +yoyaku[l][5]+ "<br>" + yoyaku[l][6];

                    // 予約詳細定義
                    var detail = "　　　　　　予約者名　　：" + yoyaku[l][0] + "<br>";
                    detail +=    "　　　　　　予約時間　　：" + yoyaku[l][4] + "-" + yoyaku[l][5] + "<br>";
                    detail +=    "　　　　　　　目的　　　：" + yoyaku[l][8] + "<br>";
                    detail +=    "　　　　　　利用者名　　：" + yoyaku[l][6] + "<br>";
                    detail +=    "　　　　　利用者連絡先　：" + yoyaku[l][7] + "<br>";
                    detail +=    "　　　　　　　備考　　　：" + yoyaku[l][9];

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
                    //calendar += "<h1>"+year+"</h1>"
                }

                //var num = use_time.length - using;
                //calendar += "<h1>"+Number(date[0])+"<br>"+Number(date[1])+"<br>"+Number(date[2])+"<br>"+month+"<br>"+dates+"</h1>";


            }
            calendar += "</td>";
            //calendar += "<td><p>a</p></td>";
        }
    }
    calendar += "</tr>";
    return calendar;
}

