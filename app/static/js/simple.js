function coladd() {
        var table = document.getElementById("table");
        // 行を行末に追加
        var row = table.insertRow(-1);
        //td分追加
        var cell1 = row.insertCell(-1);
        var cell2 = row.insertCell(-1);
        var cell3 = row.insertCell(-1);
        var cell4 = row.insertCell(-1);
        // セルの内容入力
        cell1.innerHTML = '行を追加しました';
        //cell2.innerHTML = 'この行を削除しますか？<input type="button" value=削除" id="coladd" onclick="coldel(this)">';
    }
    function coldel(obj) {
        // 削除ボタンを押下された行を取得
        tr = obj.parentNode.parentNode;
        // trのインデックスを取得して行を削除する
        tr.parentNode.deleteRow(tr.sectionRowIndex);
    }