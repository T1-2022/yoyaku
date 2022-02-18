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
    var tr_time = ["08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30"];
    //var room_name = ["0","1","2","3","4","5","6","7"];
    //yoyaku = [id, user_id, conf_id, register_name, date, starttime, endtime, user_name, user_email, purpose, remarks]

    // 日付
    calendar += "<tr><th></th>";
    for (var i = 0; i < tr_time.length; i++) {
        calendar += "<th>" + tr_time[i] + "</th>";
    }
    calendar += "</tr>";
    for (var j = 0; j < room.length; j++) {
        calendar += "<tr><th scope='row'>" + room[j][1] + "</th>";
        for (var k = 0; k < tr_time.length; k++) {
            // 予約検索
            calendar += "<td>";
            //var zure = 0;
            for (var l = 0; l < yoyaku.length; l++) {
                //予約idを取得
                var id = yoyaku[l][0];
                //dateを年月日に分割
                var date = yoyaku[l][4].split("/");
                //時間を取得
                var start_time = yoyaku[l][5];
                var end_time = yoyaku[l][6];
                //使用時間の計算
                var st_t = yoyaku[l][5].split(":"); //例）12:30
                var en_t = yoyaku[l][6].split(":"); //例) 14:00
                var use_st = Number(st_t[0]); //12
                var use_en = Number(en_t[0]); //14
                //スタート時間を数字にする
                if ( Number(st_t[1]) != 0 ){use_st += (Number(st_t[1])/60);} //12.5
                if ( Number(en_t[1]) != 0 ){use_en += (Number(en_t[1])/60);} 

                //使用時間
                var using = use_en - use_st; //1.5時間
                //必要なコマ数を計算
                var num_table = Math.ceil(using / 0.5); //3:3つのテーブルが必要

                //テーブルの表示時間を数値にする
                var tr_t = tr_time[k].split(":");
                var num_tr_t = Number(tr_t[0]);
                if ( num_table != 0 || num_table != 1){num_tr_t += 0.5;}
                if ( Number(tr_t[1]) != 0 ){num_tr_t += (Number(tr_t[1])/60);}


                //予約検索
                if ( Number(date[0]) == year
                    && Number(date[1]) == month+1
                    && Number(date[2]) == dates
                    && room[j][0] == yoyaku[l][2]
                    //&& use_time[k+1] == yoyaku[l][5]
                    && (num_tr_t) <= use_st
                    && use_st < (num_tr_t+0.5)){
                    
                    //calendar += "<h1>"+num_table+"</h1>"
                    //calendar += "<h1>"+en_t[1]+"</h1>"
                    if ( Number(en_t[1]) > 0 && Number(en_t[1] < 30) ){num_table += 1;}
                    if ( Number(en_t[1]) > 31 && Number(en_t[1] < 60) ){num_table += 1;}

                    
                    //必要なテーブルの数結合する
                    if (num_table == 2) {calendar += "<td colspan=\"2\">";}
                    else if (num_table == 3) {calendar += "<td colspan=\"3\">";}
                    else if (num_table == 4) {calendar += "<td colspan=\"4\">";}
                    else if (num_table == 5) {calendar += "<td colspan=\"5\">";}
                    else if (num_table == 6) {calendar += "<td colspan=\"6\">";}
                    else if (num_table == 7) {calendar += "<td colspan=\"7\">";}
                    else if (num_table == 8) {calendar += "<td colspan=\"8\">";}
                    else if (num_table == 9) {calendar += "<td colspan=\"9\">";}
                    else if (num_table == 10) {calendar += "<td colspan=\"10\">";}
                    else if (num_table == 11) {calendar += "<td colspan=\"11\">";}
                    else if (num_table == 12) {calendar += "<td colspan=\"12\">";}
                    else if (num_table == 13) {calendar += "<td colspan=\"13\">";}
                    else if (num_table == 14) {calendar += "<td colspan=\"14\">";}
                    else if (num_table == 15) {calendar += "<td colspan=\"15\">";}
                    else if (num_table == 16) {calendar += "<td colspan=\"16\">";}
                    else if (num_table == 17) {calendar += "<td colspan=\"17\">";}
                    else if (num_table == 18) {calendar += "<td colspan=\"18\">";}
                    else if (num_table == 19) {calendar += "<td colspan=\"19\">";}
                    else if (num_table == 20) {calendar += "<td colspan=\"20\">";}
                    else if (num_table == 21) {calendar += "<td colspan=\"21\">";}
                    else if (num_table == 22) {calendar += "<td colspan=\"22\">";}
                    else if (num_table == 23) {calendar += "<td colspan=\"23\">";}
                    else if (num_table == 24) {calendar += "<td colspan=\"24\">";}
                    else if (num_table == 25) {calendar += "<td colspan=\"25\">";}
                    //calendar += "<td colspan = \"num_table\">";

                    
                    // ボタン内容定義
                    var text = yoyaku[l][5] + "-" +yoyaku[l][6]+ "<br>" + yoyaku[l][7];

                    // 予約詳細定義
                    var detail = "　　　　　　予約者名　　：" + yoyaku[l][3] + "<br>";
                    detail +=    "　　　　　　予約時間　　：" + yoyaku[l][5] + "-" + yoyaku[l][6] + "<br>";
                    detail +=    "　　　　　　　目的　　　：" + yoyaku[l][9] + "<br>";
                    detail +=    "　　　　　　利用者名　　：" + yoyaku[l][7] + "<br>";
                    detail +=    "　　　　　利用者連絡先　：" + yoyaku[l][8] + "<br>";
                    detail +=    "　　　　　　　備考　　　：" + yoyaku[l][10];

                    // 削除できるかチェック
                    var delete_button = "";
                    if (adminFlag == true || yoyaku[l][11] == registerID) {
                        delete_button = "<button class='btn btn-secondary' type='submit' data-bs-dismiss='modal'>削除</button>";
                    }

                    // ボタン設定
                    calendar += "<button class='btn btn-secondary font-small' type='button' data-bs-toggle='modal' data-bs-target='#reserve" + id + "' ";
                    calendar += "onclick = 'setReserve(" + id + ")'>" + text + "</button>";
                    calendar += "<div class='modal fade' id='reserve";
                    calendar += yoyaku[l][0] + "' tabindex=' - 1' aria-hidden='true'>";
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
            //calendar += "<td><p>a</p></td>";
        }
    }
    calendar += "</tr>";
    return calendar;
}

// 予約内容取得
function setReserve(num) {
    var formName = "reserveID" + num;
    document.querySelector('input[id="' + formName + '"]').value = num;
}

