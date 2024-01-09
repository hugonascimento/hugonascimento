// External libraries
import * as React from 'react'
import Container from '@mui/material/Container'
// Internal libraries/utilities
import ThemeRegistry from '@/theme/themeRegistry'
// Components
import { Background } from '@/components/background'
// Stylesheets
import '@/styles/globals.css'

export const metadata = {
    title: {
        default: 'Hugo Nascimento',
    },
    description: '',
    applicationName: '',
    authors: [
        { name: 'Hugo Nascimento', url: 'https://github.com/hugonascimento' },
    ],
    creator: 'Hugo Nascimento',
    robots: {
        index: false,
        follow: false,
        nocache: true,
        googleBot: {
            index: false,
            follow: false,
            noimageindex: true,
        },
    },
}

export default function RootLayout({ children }) {
    return (
        <html lang="pt-BR">
            <body>
                <ThemeRegistry>
                    <Container
                        maxWidth="xl"
                        sx={{
                            flexGrow: 1,
                            px: 2,
                            userSelect: 'none',
                        }}
                    >
                        {children}
                    </Container>
                    <Background />
                </ThemeRegistry>
            </body>
        </html>
    )
}
