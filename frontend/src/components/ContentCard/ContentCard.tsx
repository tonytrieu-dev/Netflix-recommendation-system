import { useState } from 'react';
import { Card, CardContent, Typography, Modal, Box } from '@mui/material';
import { styled } from '@mui/material/styles';
import { ContentRecommendation } from '../../services/api';

const StyledCard = styled(Card)(() => ({
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

interface ContentCardProps {
  content: ContentRecommendation;
  contentType: string;
}

const ContentCard = ({ content, contentType }: ContentCardProps) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleCardClick = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  const contentTypeLabel = contentType === 'movies' ? 'Movie' : 'TV Show';

  return (
    <>
      <StyledCard onClick={handleCardClick}>
        <CardContent>
          <Typography variant="h6" component="div" noWrap sx={{ fontWeight: 700 }}>
            {content.title}
          </Typography>
          <Typography variant="body2" color="rgba(255,255,255,0.7)">
            Similarity: {(content.similarity * 100).toFixed(1)}%
          </Typography>
        </CardContent>
      </StyledCard>

      <Modal
        open={isModalOpen}
        onClose={handleCloseModal}
        aria-labelledby="content-modal-title"
      >
        <ModalContent>
          <Typography id="content-modal-title" variant="h5" component="h2" gutterBottom sx={{ fontWeight: 700 }}>
            {content.title}
            <Typography component="span" variant="subtitle1" sx={{ ml: 1, color: 'rgba(255,255,255,0.7)' }}>
              ({contentTypeLabel})
            </Typography>
          </Typography>
          <Typography variant="body1" sx={{ mt: 2 }}>
            {content.description}
          </Typography>
          <Typography variant="body2" sx={{ mt: 2, color: 'rgba(255,255,255,0.7)' }}>
            Similarity Score: {(content.similarity * 100).toFixed(1)}%
          </Typography>
        </ModalContent>
      </Modal>
    </>
  );
};

export default ContentCard;
