*** Settings ***
Library  ehac.py


*** variables ***
${username}   admin
${password}  Rakesh123!
${login_url}  http://10.110.26.137:8080/ehac/UI/jsf/adminLogin.xhtml
${welcome_url}  http://10.110.26.137:8080/ehac/UI/jsf/home.xhtml




*** Test Cases ***
| Login_test

  ${result} =  login_test  ${login_url}  ${username}  ${password}  ${welcome_url}

  Should be equal  ${result}   Pass


| logout_test

  ${result} =  logout_test  ${login_url}  ${username}  ${password}

  Should be equal  ${result}   Pass
