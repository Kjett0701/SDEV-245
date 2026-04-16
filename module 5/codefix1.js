// Bad code. 
//app.get('/profile/:userId', (req, res) => {
    //User.findById(req.params.userId, (err, user) => {
        //if (err) return res.status(500).send(err);
        //res.json(user);
    //});
//}); 

// Good code. 

app.get('/profile/:userId', (req, res) => {
    if (!req.user || req.user.id !== req.params.userId) {
        return res.status(403).send("Not allowed");
    }

    User.findById(req.params.userId, (err, user) => {
        res.json(user);
    });
});
