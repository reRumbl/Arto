'use client';

import { Box, Container } from '@mui/material';
import Header from './Header';
import Footer from './Footer';

type MainLayoutProps = {
    children: React.ReactNode;
};


export default function MainLayout({ children }: MainLayoutProps) {
    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
            <Header />
            <Container component='main' sx={{ mt: 4, mb: 4, flexGrow: 1 }}>
                {children}
            </Container>
            <Footer />
        </Box>
    );
}
