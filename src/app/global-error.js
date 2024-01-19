'use client'
// External libraries
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import Typography from '@mui/material/Typography'
import ArrowBackIcon from '@mui/icons-material/ArrowBack'
// Internal libraries/utilities
//
// Components
import { Background } from '@/components/background'
// Stylesheets
//

export default function GlobalError({ error }) {
    return (
        <html>
            <body>
                <Box
                    display="flex"
                    justifyContent="center"
                    alignItems="center"
                    height="100vh"
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
                <Background />
            </body>
        </html>
    )
}
