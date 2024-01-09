// External libraries
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

export default function NotFound() {
    return (
        <>
            <Box
                display="flex"
                justifyContent="center"
                alignItems="center"
                height="80vh"
            >
                <Box>
                    <Typography variant="h6" align="center">
                        Essa página não existe 🙁
                    </Typography>
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
        </>
    )
}
