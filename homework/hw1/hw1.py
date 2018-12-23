"""
CENT 110
Craig Opie
hw1.py

Algorithm
Python program that uses the print function to write the contents of what would 
be a simple HTML document using the indentation scheme and format shown below.

<html>
  <head>
    <title>Craig Opie's hobbies</title>
  </head>
  <body>
    <h1>My Hobbies</h1>
    <table border="1">
      <tr>
        <th>Hobby</th> <th>Number of Years</th>
      </tr>
      <tr>
        <td>Gambling</td> <td>13</td>
      </tr>
      <tr>
        <td>Traveling</td> <td>12</td>
      </tr>
      <tr>
        <td>Hiking</td> <td>5</td>
      </tr>
    </table>
  </body>
</html>
"""

# The following print function demonstrates a 'block' string litteral which  
# includes formatting
print("""<html>
  <head>
    <title>Craig Opie's hobbies</title>
  </head>
  <body>
    <h1>My Hobbies</h1>
    <table border="1">
      <tr>
        <th>Hobby</th> <th>Number of Years</th>
      </tr>
      <tr>
        <td>Gambling</td> <td>13</td>
      </tr>
      <tr>
        <td>Traveling</td> <td>12</td>
      </tr>
      <tr>
        <td>Hiking</td> <td>5</td>
      </tr>
    </table>
  </body>
</html>
""")
