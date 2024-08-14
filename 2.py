Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bucky roberts
SyntaxError: invalid syntax
>>> "roberts bucky"
'roberts bucky'
>>> 'bucky roberts is awesome!'
'bucky roberts is awesome!'
>>> I dont't think shes 18'
SyntaxError: invalid syntax
>>> "I dont't think shes 18"
"I dont't think shes 18"
>>> 'Í don/'t think shes 18'
SyntaxError: unterminated string literal (detected at line 1)
>>> 'I dont/ t' think shes 18'
SyntaxError: unterminated string literal (detected at line 1)
>>> SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: invalid syntax
>>> 
================================ RESTART: Shell ================================
>>> 'I dont\'t think shes 18'
"I dont't think shes 18"
>>> print("hey now brown cow")
hey now brown cow
>>> print('C:bucky\desktop\nmpics')
C:bucky\desktop
mpics
>>> print(r'C:bucky\desktop\nmpics')
C:bucky\desktop\nmpics
>>> firstname = "jack"
>>> firstname + "oggy"
'jackoggy'
>>> firstname * 10
'jackjackjackjackjackjackjackjackjackjack'
