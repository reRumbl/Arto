import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import { AppRouterCacheProvider } from '@mui/material-nextjs/v15-appRouter';
import ThemeProvider from '@/components/ThemeProvider';
import MainLayout from '@/components/layout/MainLayout';
import './globals.css';

const geistSans = Geist({
    variable: '--font-geist-sans',
    subsets: ['latin'],
});

const geistMono = Geist_Mono({
    variable: '--font-geist-mono',
    subsets: ['latin'],
});

export const metadata: Metadata = {
    title: 'Arto',
    description: 'A website for posting and discussing news',
};


export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang='en'>
            <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
                <AppRouterCacheProvider>
                    <ThemeProvider>
                        <MainLayout>{children}</MainLayout>
                    </ThemeProvider>
                </AppRouterCacheProvider>
            </body>
        </html>
    );
}
