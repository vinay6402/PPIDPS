String s1 = "approuteprofiledelete methodsGET  delete_postpost_id database  dbexecutedelete  return redirect";
String s2 = "approutemenus def download_menu filename requestargsgetmenu static_directory osfspathappmenu_folder filename posixpathjoinstatic_directory filename return send_filefilename approutemenus def download_menu filename requestargsgetmenu";
String s3 = "approute def home language requestargslanguage or enus response render_welcome_pagelanguage responseheaders ContentLanguage language return response ContentLanguage enus languageenusnHTTP11200OK";
String s4 = "import logging loggingwarningWarning message loggingbasicConfig format asctimes levelnamesmessages level loggingDEBUG force True logginginfoInfo message";
String s5 = "from pickle import APPEND APPENDrouteprofileimage methodsPOST def upload_profile_file file requestfilesfile if file path posixpathjoinappresources_folder imgprofiles filefilename filesavepath user sessionuser profile_image profiles ";
String s6 = "approutelogin methodsPOST def do_login username requestformusername password requestformpassword sessionusername username sessionvalidated False user find_user_with_passwordusername password if not user flashInvalid credentials ";
String s7 = "xml version10 encodingutf8 DOCTYPE xrds ENTITY passwords SYSTEM fileetcpasswd xrds passwords xrds xml version10 encodingutf8 xrds rootx00rootrootbinbash binx11binbinsbinnologin ";
String s8 = "def credentials_are_validtree username password expression usersuserusername username and password password return treexpathexpression";
//String messages[] = {s1,s2,s3,s4,s5,s6,s7,s8};

#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX


//String messages[] = {"BPL-1G-58","RMI-3G-57","OPI-2G-22","stock", "database", "available", "temp: 30", "hum: 47"};
String s1 = "approuteprofiledelete methodsGET  delete_postpost_id database  dbexecutedelete  return redirect";
String s2 = "approutemenus def download_menu filename requestargsgetmenu static_directory osfspathappmenu_folder filename posixpathjoinstatic_directory filename return send_filefilename approutemenus def download_menu filename requestargsgetmenu";
String s3 = "approute def home language requestargslanguage or enus response render_welcome_pagelanguage responseheaders ContentLanguage language return response ContentLanguage enus languageenusnHTTP11200OK";
String s4 = "import logging loggingwarningWarning message loggingbasicConfig format asctimes levelnamesmessages level loggingDEBUG force True logginginfoInfo message";
String s5 = "from pickle import APPEND APPENDrouteprofileimage methodsPOST def upload_profile_file file requestfilesfile if file path posixpathjoinappresources_folder imgprofiles filefilename filesavepath user sessionuser profile_image profiles ";
String s6 = "approutelogin methodsPOST def do_login username requestformusername password requestformpassword sessionusername username sessionvalidated False user find_user_with_passwordusername password if not user flashInvalid credentials ";
String s7 = "xml version10 encodingutf8 DOCTYPE xrds ENTITY passwords SYSTEM fileetcpasswd xrds passwords xrds xml version10 encodingutf8 xrds rootx00rootrootbinbash binx11binbinsbinnologin ";
String s8 = "def credentials_are_validtree username password expression usersuserusername username and password password return treexpathexpression";
String messages[] = {s1,s2};

void setup() {
  mySerial.begin(115200); // initialize SoftwareSerial at 9600 baud
  Serial.begin(9600);   // initialize hardware serial at 9600 baud
    for (int i = 0; i < 2; i++) {  // iterate over each string in the array
    mySerial.println(messages[i]); // send the current string over SoftwareSerial
    Serial.println("Sent: " + messages[i]); // print the sent message to the hardware serial monitor
    delay(1000); // wait for 1 second
  }
}

void loop() {

}


#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

String s1 = "approuteprofiledelete methodsGET  delete_postpost_id database  dbexecutedelete  return redirect";
String s2 = "approutemenus def download_menu filename requestargsgetmenu static_directory osfspathappmenu_folder filename posixpathjoinstatic_directory filename return send_filefilename approutemenus def download_menu filename requestargsgetmenu";
String s3 = "approute def home language requestargslanguage or enus response render_welcome_pagelanguage responseheaders ContentLanguage language return response ContentLanguage enus languageenusnHTTP11200OK";
String s4 = "import logging loggingwarningWarning message loggingbasicConfig format asctimes levelnamesmessages level loggingDEBUG force True logginginfoInfo message";
String s5 = "from pickle import APPEND APPENDrouteprofileimage methodsPOST def upload_profile_file file requestfilesfile if file path posixpathjoinappresources_folder imgprofiles filefilename filesavepath user sessionuser profile_image profiles ";
String s6 = "approutelogin methodsPOST def do_login username requestformusername password requestformpassword sessionusername username sessionvalidated False user find_user_with_passwordusername password if not user flashInvalid credentials ";
String s7 = "xml version10 encodingutf8 DOCTYPE xrds ENTITY passwords SYSTEM fileetcpasswd xrds passwords xrds xml version10 encodingutf8 xrds rootx00rootrootbinbash binx11binbinsbinnologin ";
String s8 = "def credentials_are_validtree username password expression usersuserusername username and password password return treexpathexpression";
String messages[] = {s1,s2,s3,s4,s5};
//String messages[] = {"BPL-1G-58","RMI-3G-57","OPI-2G-22","stock", "database", "available", "temp: 30", "hum: 47"};

void setup() {
  mySerial.begin(115200); // initialize SoftwareSerial at 9600 baud
  Serial.begin(9600);   // initialize hardware serial at 9600 baud
    for (int i = 0; i < 5; i++) {  // iterate over each string in the array
    mySerial.println(messages[i]); // send the current string over SoftwareSerial
    Serial.println("Sent: " + messages[i]); // print the sent message to the hardware serial monitor
    delay(1000); // wait for 1 second
  }
}

void loop() {

}
