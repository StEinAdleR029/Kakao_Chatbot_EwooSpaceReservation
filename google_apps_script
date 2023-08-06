function onEditTrigger(e) {
  var gas = SpreadsheetApp.getActiveSheet();
  var currentCell = gas.getActiveCell();
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName('실시간 공간 예약 현황');


  if (currentCell.getColumn() == 11) { // 입력을 감지할 셀 설정 : 1=A열, 2=B열....
    var email = currentCell.offset(0, -2); //입력 감지 셀 기준으로 날짜를 기입할 셀 위치 선택 (세로, 가로)
    var purpose = currentCell.offset(0,-3)
    var space = currentCell.offset(0,-4)
    var time = currentCell.offset(0,-5)
    var date = currentCell.offset(0,-6)
    var name = currentCell.offset(0,-7)
    var school_num = currentCell.offset(0,-8)
    var apply_time = currentCell.offset(0,-9)
    var reason = currentCell.offset(0, 1);
    var debug = currentCell.offset(0, 2);
    var accept = currentCell.offset(0,0)

    var data_email = email.getValue(); // 수정: getValue() 추가
    var data_reason = reason.getValue(); // 수정: getValue() 추가
    var data_purpose = purpose.getValue();
    var data_space = space.getValue();
    var data_time = time.getValue();
    var data_date = date.getValue();
    var data_name = name.getValue();
    var data_school_num = school_num.getValue()
    var data_apply_time = apply_time.getValue()
    var data_accept = accept.getValue()

    var emailAddress = data_email;
    var subject = '안녕하세요. 공간예약과 관련하여 승인여부를 말씀드립니다.';
    var message = '안녕하세요, <strong>' + data_name + '님</strong><br><br><strong>' 
      + data_school_num + ' ' + data_name + '님</strong>께서는 '
      + data_apply_time + '에 <br><br>  <strong>"' + data_purpose + '"</strong> 목적으로 ' 
      + data_date + ' <strong>' + data_time + '</strong>에 <strong>' + data_space 
      + '</strong>에서 <br><br> 공간 예약을 신청하셨습니다. <br><br>공간예약이 정상적으로 "<strong>' 
      + data_accept + '"</strong>되었음을 알려드립니다. <br><br>공간예약이 거절되었다면 사유는 <strong>"'
      + data_reason + '</strong>"입니다. <br><hr><br>자세한 사항은 교무부 최대호에게 문의하시기 바랍니다.';

    debug.setValue("메시지 전송 중.");

    MailApp.sendEmail({
      to: emailAddress,
      subject: subject,
      htmlBody: message // Set the message as an HTML body to allow formatting
    });

    debug.setValue("메시지가 전송되었습니다.");

    // Rest of the code...
  }
}
