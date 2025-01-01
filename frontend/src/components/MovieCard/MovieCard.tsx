import { useState } from 'react';
import { Card, CardContent, Typography, Modal, Box } from '@mui/material';
import { styled } from '@mui/material/styles';
import { MovieRecommendation } from '../../services/api';

const StyledCard = styled(Card)(({ theme }) => ({
  backgroundColor: '#181818',
  color: 'white',
  transition: 'transform 0.2s ease-in-out',
  cursor: 'pointer',
  '&:hover': {
    transform: 'scale(1.05)',
    backgroundColor: '#282828',
  },
}));

const ModalContent = styled(Box)({
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: '80%',
  maxWidth: '600px',
  backgroundColor: '#181818',
  color: 'white',
  borderRadius: '4px',
  padding: '20px',
  outline: 'none',
});

interface MovieCardProps {
  movie: MovieRecommendation;
}

const MovieCard = ({ movie }: MovieCardProps) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleCardClick = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      <StyledCard onClick={handleCardClick}>
        <CardContent>
          <Typography variant="h6" component="div" noWrap>
            {movie.title}
          </Typography>
          <Typography variant="body2" color="rgba(255,255,255,0.7)">
            Similarity: {(movie.similarity * 100).toFixed(1)}%
          </Typography>
        </CardContent>
      </StyledCard>

      <Modal
        open={isModalOpen}
        onClose={handleCloseModal}
        aria-labelledby="movie-modal-title"
      >
        <ModalContent>
          <Typography id="movie-modal-title" variant="h5" component="h2" gutterBottom>
            {movie.title}
          </Typography>
          <Typography variant="body1" sx={{ mt: 2 }}>
            {movie.description}
          </Typography>
          <Typography variant="body2" sx={{ mt: 2, color: 'rgba(255,255,255,0.7)' }}>
            Similarity Score: {(movie.similarity * 100).toFixed(1)}%
          </Typography>
        </ModalContent>
      </Modal>
    </>
  );
};

export default MovieCard;
