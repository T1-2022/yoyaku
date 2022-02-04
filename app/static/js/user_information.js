/*
    created at 2022/02/03
    created by shinoda hiroki

    ユーザー情報変更ページへのスクリプト
*/

/* ユーザーネーム変更ページへの遷移 */
let change_user_name_btn = document.getElementById('change_user_name_btn');
// クリックされた際にページ遷移
change_user_name_btn.childNodes[1].onclick = function (){
    document.location.href = '/user_info/change_name';
};

/* メイルアドレス変更ページへの遷移 */
let change_user_mail_btn = document.getElementById('change_user_mail_btn');
// クリックされた際にページ遷移
change_user_mail_btn.childNodes[1].onclick = function to_change_user_mail_page(){
    document.location.href = '/user_info/change_mail';
};

/* パスワード変更ページへの遷移 */
let change_user_passwd_btn = document.getElementById('change_user_passwd_btn');
// クリックされた際にページ遷移
change_user_passwd_btn.childNodes[1].onclick = function to_change_user_passwd_page(){
    document.location.href = '/user_info/change_passwd';
};

