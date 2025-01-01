import { useState } from 'react';
import { Container, Typography, Box, Alert, CircularProgress } from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import SearchBar from './components/SearchBar/SearchBar';
import RecommendationList from './components/RecommendationList/RecommendationList';
import { getRecommendations } from './services/api';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#e50914',
    },
    background: {
      default: '#141414',
      paper: '#181818',
    },
  },
  typography: {
    fontFamily: [
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif',
    ].join(','),
  },
});

function App() {
  const [recommendations, setRecommendations] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (query: string) => {
    setError(null);
    setLoading(true);
    try {
      const data = await getRecommendations(query);
      setRecommendations(data.recommendations);
    } catch (err: any) {
      setError(err.message);
      setRecommendations([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container maxWidth="lg">
        <Box sx={{ py: 4 }}>
          <Typography
            variant="h3"
            component="h1"
            sx={{
              mb: 4,
              fontWeight: 600,
              textAlign: 'center',
              color: 'white',
            }}
          >
            Netflix Recommendation System
          </Typography>

          <Box sx={{ maxWidth: 600, mx: 'auto', mb: 4 }}>
            <SearchBar onSearch={handleSearch} />
          </Box>

          {error && (
            <Alert severity="error" sx={{ mb: 3 }}>
              {error}
            </Alert>
          )}

          {loading ? (
            <Box
              sx={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                minHeight: '200px',
              }}
            >
              <CircularProgress />
            </Box>
          ) : (
            recommendations.length > 0 && (
              <RecommendationList recommendations={recommendations} />
            )
          )}
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;
