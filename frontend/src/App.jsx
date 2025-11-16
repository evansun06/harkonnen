import { useState, useEffect } from 'react';
import { Search } from 'lucide-react';

export default function HarkonnenHome() {
  const [searchValue, setSearchValue] = useState('');
  const [opacity, setOpacity] = useState(1);

  useEffect(() => {
    let direction = -1; // -1 for fading out, 1 for fading in
    
    const interval = setInterval(() => {
      setOpacity(prev => {
        const newOpacity = prev + (direction * 0.02);
        
        // Switch direction at boundaries
        if (newOpacity <= 0.3) {
          direction = 1;
          return 0.3;
        }
        if (newOpacity >= 1) {
          direction = -1;
          return 1;
        }
        
        return newOpacity;
      });
    }, 50);
    
    return () => clearInterval(interval);
  }, []);

  const styles = {
    container: {
      minHeight: '100vh',
      width: '100vw',
      background: 'linear-gradient(to bottom right, #18181b, #57534e, #262626)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      position: 'relative',
      overflow: 'hidden',
      margin: 0,
      padding: 0,
      boxSizing: 'border-box'
    },
    backgroundPattern: {
      position: 'absolute',
      inset: 0,
      opacity: 0.1,
      backgroundImage: `repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(156, 163, 175, 0.1) 2px,
        rgba(156, 163, 175, 0.1) 4px
      )`
    },
    content: {
      zIndex: 10,
      width: '100%',
      maxWidth: '56rem',
      padding: '0 1.5rem'
    },
    title: {
      fontFamily: 'Raleway, sans-serif',
      fontWeight: 200,
      fontSize: 'clamp(3rem, 8vw, 6rem)',
      textAlign: 'center',
      marginBottom: '4rem',
      textTransform: 'uppercase',
      transform: 'scaleX(1.6)',
      background: 'linear-gradient(135deg, #e5e5e5 0%, #a3a3a3 50%, #d4d4d4 100%)',
      WebkitBackgroundClip: 'text',
      WebkitTextFillColor: 'transparent',
      backgroundClip: 'text',
      textShadow: '0 0 40px rgba(229, 229, 229, 0.2)',
      letterSpacing: '0.2em'
    },
    searchContainer: {
      position: 'relative',
      opacity: opacity
    },
    searchWrapper: {
      position: 'relative'
    },
    searchGlow: {
      position: 'absolute',
      inset: '-4px',
      background: 'linear-gradient(to right, #52525b, #9ca3af, #52525b)',
      borderRadius: '1rem',
      filter: 'blur(8px)',
      opacity: 0.25,
      transition: 'opacity 0.5s'
    },
    searchBox: {
      position: 'relative',
      display: 'flex',
      alignItems: 'center',
      background: 'linear-gradient(to right, #27272a, #262626)',
      borderRadius: '1rem',
      border: '1px solid #52525b',
      boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
      overflow: 'hidden'
    },
    searchIcon: {
      marginLeft: '1.5rem',
      color: '#9ca3af',
      flexShrink: 0
    },
    input: {
      width: '100%',
      padding: '1.5rem',
      background: 'transparent',
      color: '#e5e7eb',
      border: 'none',
      outline: 'none',
      letterSpacing: '0.2em',
      textTransform: 'uppercase',
      fontSize: '1.125rem',
      fontFamily: 'Orbitron, monospace',
      transform: 'scaleX(1.3)',
      transformOrigin: 'left'
    },
    divider: {
      height: '3rem',
      width: '1px',
      background: 'linear-gradient(to bottom, transparent, #6b7280, transparent)',
      marginRight: '1rem'
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.backgroundPattern} />

      <div style={styles.content}>
        <h1 style={styles.title}>
          HARKONNEN
        </h1>

        <div style={styles.searchContainer}>
          <div style={styles.searchWrapper}>
            <div style={styles.searchGlow} />
            
            <div style={styles.searchBox}>
              <div style={styles.searchIcon}>
                <Search size={24} />
              </div>
              
              <input
                type="text"
                value={searchValue}
                onChange={(e) => setSearchValue(e.target.value)}
                placeholder="INITIALIZE SEARCH PROTOCOL..."
                style={styles.input}
              />

              <div style={styles.divider} />
            </div>
          </div>
        </div>
      </div>

      <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Raleway:wght@200;300&display=swap" rel="stylesheet" />
    </div>
  );
}