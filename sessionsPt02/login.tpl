<html>
<body>
    <h1>Login</h1>
    <form action="/login" method="post">
        <hr/>
        <table>
            <tr>
                <td><em>Name</em></td>
                <td><input type="text" name="username"/><br></td>
            </tr>
            <tr>
                <td><em>Password</em></td>
                <td><input type="password" name="password"/></td>
            </tr>
            <tr>
                <td><em>Favorite color</em></td>
                <td><input type="text" name="favcolor"/></td>
            </tr>
        </table>
        <hr/>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>