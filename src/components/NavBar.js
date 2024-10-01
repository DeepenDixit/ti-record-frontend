import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@material-ui/core';

function NavBar() {
    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" style={{ flexGrow: 1 }}>
                    <a href="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                        TI Record Filter Utility
                    </a>
                </Typography>
                <Button color="inherit" href="/logout">Logout</Button>
            </Toolbar>
        </AppBar>
    );
}

export default NavBar;