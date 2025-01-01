import { useState, KeyboardEvent } from 'react';
import { TextField, InputAdornment, IconButton, Box, Select, MenuItem, FormControl, InputLabel } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { styled } from '@mui/material/styles';

const StyledTextField = styled(TextField)(() => ({
  '& .MuiInputBase-root': {
    color: 'white',
    backgroundColor: '#333',
    borderRadius: '4px',
    '&:hover': {
      backgroundColor: '#404040',
    },
    '& fieldset': {
      borderColor: 'transparent',
    },
    '&:hover fieldset': {
      borderColor: 'transparent',
    },
    '&.Mui-focused fieldset': {
      borderColor: '#e50914',
    },
  },
  '& .MuiInputBase-input': {
    padding: '12px 14px',
  },
}));

const StyledSelect = styled(Select)(() => ({
  '& .MuiSelect-select': {
    color: 'white',
    backgroundColor: '#333',
  },
  '& .MuiOutlinedInput-notchedOutline': {
    borderColor: 'transparent',
  },
  '&:hover .MuiOutlinedInput-notchedOutline': {
    borderColor: 'transparent',
  },
  '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
    borderColor: '#b20710',
  },
  '& .MuiSelect-icon': {
    color: 'white',
  },
  '& .MuiMenu-paper': {
    backgroundColor: '#141414',
  },
  '& .MuiMenuItem-root:hover': {
    backgroundColor: '#b20710',
  }
}));

const StyledFormControl = styled(FormControl)(() => ({
  '& .MuiInputLabel-root': {
    color: 'rgba(255, 255, 255, 0.7)',
    '&.Mui-focused': {
      color: '#e50914',
    },
  },
  '& .MuiFormLabel-root': {
    transform: 'translate(0, -20px) scale(0.85)',
    '&.MuiInputLabel-shrink': {
      transform: 'translate(0, -20px) scale(0.85)',
    },
  },
}));

interface SearchBarProps {
  onSearch: (query: string, recommendationCount: number) => void;
}

const SearchBar = ({ onSearch }: SearchBarProps) => {
  const [query, setQuery] = useState('');
  const [recommendationCount, setRecommendationCount] = useState(5);

  const handleSearch = () => {
    if (query.trim()) {
      onSearch(query.trim(), recommendationCount);
    }
  };

  const handleKeyPress = (event: KeyboardEvent<HTMLDivElement>) => {
    if (event.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <Box sx={{ display: 'flex', gap: 2, alignItems: 'flex-start' }}>
      <Box sx={{ flex: 1 }}>
        <StyledTextField
          fullWidth
          placeholder="Enter a movie or TV show title..."
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          onKeyPress={handleKeyPress}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton onClick={handleSearch} sx={{ color: 'white' }}>
                  <SearchIcon />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
      </Box>
      <StyledFormControl sx={{ minWidth: 200 }}>
        <InputLabel 
          id="recommendation-count-label"
          sx={{ 
            position: 'relative',
            transform: 'none',
            marginBottom: 1
          }}
        >
          Number of recommendations
        </InputLabel>
        <StyledSelect
          labelId="recommendation-count-label"
          value={recommendationCount}
          onChange={(event) => setRecommendationCount(Number(event.target.value))}
          label="Number of recommendations"
        >
          <MenuItem value={2}>2 recommendations</MenuItem>
          <MenuItem value={3}>3 recommendations</MenuItem>
          <MenuItem value={4}>4 recommendations</MenuItem>
          <MenuItem value={5}>5 recommendations</MenuItem>
          <MenuItem value={10}>10 recommendations</MenuItem>
        </StyledSelect>
      </StyledFormControl>
    </Box>
  );
};

export default SearchBar;
