import { useState, KeyboardEvent } from 'react';
import { TextField, InputAdornment, IconButton, Box, Select, MenuItem, FormControl, InputLabel } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { styled } from '@mui/material/styles';

const StyledTextField = styled(TextField)(({ theme }) => ({
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

const StyledSelect = styled(Select)(({ theme }) => ({
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
      <FormControl sx={{ minWidth: 200 }}>
        <InputLabel sx={{ color: 'white' }}>Number of Recommendations</InputLabel>
        <StyledSelect
          value={recommendationCount}
          onChange={(event) => setRecommendationCount(Number(event.target.value))}
          label="Number of Recommendations"
        >
          <MenuItem value={5}>5 Recommendations</MenuItem>
          <MenuItem value={10}>10 Recommendations</MenuItem>
          <MenuItem value={15}>15 Recommendations</MenuItem>
          <MenuItem value={20}>20 Recommendations</MenuItem>
        </StyledSelect>
      </FormControl>
    </Box>
  );
};

export default SearchBar;
