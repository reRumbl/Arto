'use client';

import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import Link from 'next/link';


export default function Header() {
    return (
        <AppBar position='static'>
            <Toolbar>
                <Typography variant='h6' component='div' sx={{ flexGrow: 1 }}>
                    <Link href='/' passHref style={{ textDecoration: 'none', color: 'inherit' }}>
                        Arto
                    </Link>
                </Typography>
                <Box>
                    <Button color='inherit' component={Link} href='/login'>
                        Login
                    </Button>
                    <Button color='inherit' component={Link} href='/register'>
                        Register
                    </Button>
                </Box>
            </Toolbar>
        </AppBar>
    );
}
