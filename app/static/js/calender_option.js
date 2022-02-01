document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
         initialView: 'dayGridMonth',// オプション　（月表示）
         locale : 'ja',
        headerToolbar: {
                    left: 'title',
                    center: 'dayGridMonth,timeGridWeek,listWeek',
                    right: 'prev,today,next'
                },
        buttonText: {
                    prev:     '<',
                    next:     '>',
                    prevYear: '<<',
                    nextYear: '>>',
                    today:    '今日',
                    month:    '月',
                    week:     '週',
                    day:      '日',
                    list:     '一覧'
                },

        eventSources: [
			{
				googleCalendarApiKey: 'XXXXX',
				googleCalendarId: 'japanese__ja@holiday.calendar.google.com',
				rendering: 'background',
				color:"#ffd0d0"
			}
		],
         events: [
        {
            id: 'a',
            title: 'イベント',
            start: '2022-01-15'
        }
  ]
    });
    calendar.render();　// カレンダーの初期化（再レンダリング）
});