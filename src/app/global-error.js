'use client'
// External libraries
import { useEffect } from 'react'
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import Typography from '@mui/material/Typography'
import ArrowBackIcon from '@mui/icons-material/ArrowBack'
// Internal libraries/utilities
//
// Components
//
// Stylesheets
//

export default function GlobalError({ error }) {
    useEffect(() => {
        // Log the error to an error reporting service
        console.error(error)
    }, [error])

    return (
        <html>
            <body>
                <Box
                    display="flex"
                    justifyContent="center"
                    alignItems="center"
                    height="80vh"
                >
                    <Box>
                        <Typography variant="h6" align="center">
                            Erro no servidor
                        </Typography>
                        <Typography align="center">{error}</Typography>
                        <Box sx={{ pt: 10, textAlign: 'center' }}>
                            <Button
                                startIcon={<ArrowBackIcon fontSize="small" />}
                                sx={{
                                    textTransform: 'none',
                                }}
                                variant="gradient"
                                href="/"
                            >
                                Página Inicial
                            </Button>
                        </Box>
                    </Box>
                </Box>
            </body>
        </html>
    )
}
