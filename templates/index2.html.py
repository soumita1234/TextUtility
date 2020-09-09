!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Template is Working</title>
</head>
<body>
<h1>Welcome To The Text Analyazer</h1>
<br>
<h2>Enter Tour Text Here</h2>
<form action='/analyze' method='get'>
<textarea name='text' style='margin: 0px; width: 714px; height: 193px;'></textarea>
<br>
    <input type='checkbox' name='removepunc'>Remove Punctuations<br>
    <input type='checkbox' name='fullcaps'>UPPERCASE<br>
    <input type='checkbox' name='newlineremove'>New Line Remover<br>
    <input type='checkbox' name='extraspaceremove'>Extra space Remover<br>
    <input type='checkbox' name='charcount'>Character Counter<br>


<button type='submit'>Analyze Text</button>
</form>

</body>
</html>