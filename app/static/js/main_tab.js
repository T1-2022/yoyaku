
// 初期表示
window.onload = function () {
    var button = "";

    if (userInfo.admin) {
        // ボタン設定
        button += "<button class='btn btn-info' type='button' onclick='push()'>";
        button += "管理者画面へ";
        button += "</button>";
    }

    document.querySelector('#adminButton').innerHTML = button;
};

// ボタン処理
function push() {
    window.location.href = '/admin_main/';
}
