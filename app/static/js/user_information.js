/*
    created at 2022/02/03
    created by shinoda hiroki

    ユーザー情報変更ページへのスクリプト
*/

/* ユーザーネーム変更ページへの遷移 */
function to_change_user_name_page(){
    document.location.href = '/user_info/change_name';
}

/* メイルアドレス変更ページへの遷移 */
function to_change_user_mail_page(){
    document.location.href = '/user_info/change_mail';
}

/* パスワード変更ページへの遷移 */
function to_change_user_passwd_page(){
    document.location.href = '/user_info/change_passwd';
}