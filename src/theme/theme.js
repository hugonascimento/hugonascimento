// Bibliotecas externas
import { Roboto } from 'next/font/google'
import { createTheme } from '@mui/material/styles'
import { deepPurple } from '@mui/material/colors'
// Bibliotecas/utilitários internos
//
// Componentes
//
// Stylesheets
//

const roboto = Roboto({
    weight: ['300', '400', '500', '700'],
    subsets: ['latin'],
    display: 'swap',
})

const theme = createTheme({
    breakpoints: {
        values: {
            xs: 0,
            sm: 600,
            md: 900,
            lg: 1200,
            xl: 1536, //xl: 1920,
        },
    },
    palette: {
        mode: 'dark',
        primary: {
            main: '#470093', //'rgb(0, 255, 255)', //'#9885ff',
        },
        secondary: {
            main: '#470093', // #3800e1 with transparency (all icons)
        },
        text: {
            primary: '#a5a5a5',
            secondary: '#727272',
            link: '#9885ff',
        },
        background: {
            default: '#000',
            paper: 'rgba(13, 13, 13, 0.5)',
            dark: 'rgba(6, 6, 6, 0.8)',
        },
        border: {
            primary: '#1c1c1c',
        },
        divider: '#1c1c1c', //'#2d2d2d',
    },
    typography: {
        fontFamily: roboto.style.fontFamily,
    },
    components: {
        MuiAppBar: {
            styleOverrides: {
                root: {
                    backgroundImage: 'unset',
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                },
            },
        },
        MuiBackdrop: {
            styleOverrides: {
                root: {
                    backgroundImage: 'unset',
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                },
            },
        },
        MuiButton: {
            variants: [
                {
                    props: { variant: 'gradient' },
                    style: {
                        textTransform: 'none',
                        padding: '12px 20px',
                        color: '#a5a5a5',
                        background:
                            'linear-gradient(90deg,rgba(84, 29, 143, 0.3) 0%,rgba(84, 29, 143, 0.5) 25%, rgba(84, 29, 143, 0.8) 50%, rgba(84, 29, 143, 0.5) 75%, rgba(84, 29, 143, 0.3) 100%)',
                    },
                },
            ],
        },
    }
})

export default theme
