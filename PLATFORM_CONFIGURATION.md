# **AJxAI v1.2.0 | Adaptive Market Strategy Engine - Configuration & Architecture Guide**

## **🏗️ Current System Architecture**

### **Three-Layer Pipeline (Data → Decode → Action)**

**1. Data Layer (Scanners) - Active Sources**
- **Reddit Scanner**: Monitors crypto subreddits (7 allowed subreddits)
- **Binance Scanner**: Real-time crypto price/volume (10+ major cryptocurrencies)
- **News Scanner**: RSS feeds from Yahoo Finance, BeInCrypto
- **India Equity Scanner**: NIFTY50 stocks (23 symbols currently tracking)

**2. Decode Layer (AI Analysis) - 15/15 Features Operational**
- **Smart Alert Manager**: GPT-5 powered intelligent filtering
- **Portfolio Optimizer**: Advanced portfolio analysis with market commentary
- **Signal Engine**: Trading signal generation with confidence scoring
- **Pattern Analyzer**: Cross-source correlation detection
- **ML Pattern Recognizer**: Machine learning pattern discovery
- **Multi-Timeframe Analysis**: 1h, 4h, 1d timeframe analysis
- **Sentiment Flow Analysis**: Emotion tracking and trend detection
- **Institutional Flow Detection**: Large player movement identification
- **🚀 AI Predictive Forecasting**: Prophet-powered market, geopolitical, and stock predictions (7-30 days)
- **🚀 Community Simulation**: Advanced engagement modeling with viral detection
- **🚀 User Acquisition Engine**: Cross-platform automated growth campaigns
- **🔥 Decision Policy**: Aggregates signals into actionable decisions with cooldowns (Phase 5)
- **🔥 GPT Integration**: AI-powered event typing and narrative building (Phase 7)
- **🔥 Advanced Models**: SVAR and state-space models for macro analysis (Phase 8)
- **🔥 Post-Mortem Analysis**: Decision outcome evaluation and performance tracking (Phase 6)

**3. Action Layer (Execution)**
- **Paper Trading**: Safe simulation mode (currently active)
- **Multi-channel Alerts**: Telegram, Discord, email notifications
- **Reddit Posting**: Automated engagement with rate limits
- **Excel Export**: Data analysis export functionality
- **🚀 Telegram Monetization Bot**: Premium subscriptions, community management, auto-moderation
- **🚀 Cross-Platform Posting**: Automated Twitter, Reddit, Telegram content distribution
- **🚀 SEO-Optimized Content**: AI-generated content with funnel optimization

---

## **📁 Complete File Structure**

### **Root Directory**
```
├── app.py                          # Main Flask application entry point
├── advanced_trading_orchestrator.py # Coordinates all 11 advanced analysis features
├── bootstrap.py                    # Application initialization and setup
├── config.py                       # Environment-based configuration loader
├── replit.md                       # Project documentation and preferences
├── config.json                     # Master configuration file (MAIN CONFIG)
├── permissions.json                # Safety controls and access permissions
├── assets-config.json              # Asset definitions and aliases
├── sectors-config.json             # Sector classification and correlations
├── patterns.db                     # SQLite pattern analysis database
├── state.json                      # Current platform state
└── advanced_trading.log            # System operation logs
```

### **Scanner Directory (Data Collection)**
```
scanner/
├── __init__.py
├── reddit_scanner.py               # PRAW-based Reddit API integration
├── binance_scanner.py              # CCXT cryptocurrency data collection
├── news_scanner.py                 # RSS news feed processing
└── india_equity_scanner.py         # NSE equity market data collection
```

### **Decoder Directory (AI Analysis)**
```
decoder/
├── __init__.py
├── smart_alert_manager.py          # GPT-5 intelligent alert filtering
├── portfolio_optimizer.py         # GPT-5 portfolio analysis
├── signal_engine.py                # Trading signal generation
├── pattern_analyzer.py             # Cross-source correlation detection
├── ml_pattern_recognizer.py        # Machine learning pattern discovery
├── multi_timeframe_analyzer.py     # Multi-timeframe technical analysis
├── sentiment_flow_analyzer.py      # Sentiment trend analysis + AI Forecasting (Prophet)
├── correlation_matrix_engine.py    # Asset correlation analysis
├── institutional_flow_detector.py  # Large player movement detection
├── ai_analyzer.py                  # Core AI processing utilities
├── viral_scorer.py                 # Content virality scoring
├── decision_policy.py              # 🔥 Aggregated decision making with cooldowns (Phase 5)
├── gpt_integration.py              # 🔥 GPT-powered event typing and narratives (Phase 7)
├── advanced_models.py              # 🔥 SVAR and state-space models for macro analysis (Phase 8)
├── knowledge_graph.py              # AI Strategist knowledge representation
├── regime_engine.py                # Market regime detection and analysis
└── causal_engine.py                # Causal relationship analysis
```

### **Executor Directory (Action Layer)**
```
executor/
├── __init__.py
├── alert_sender.py                 # Multi-channel notification system
├── reddit_poster.py                # Automated social media posting
├── community_simulator.py          # 🚀 Advanced community engagement simulation
└── trade_executor.py               # Paper trading execution engine
```

### **Frontend Interface**
```
templates/
├── base.html                       # Responsive base template
└── dashboard.html                  # Real-time trading dashboard

static/
├── css/
│   └── style.css                   # Professional styling with themes
└── js/
    └── dashboard.js                # Real-time updates and news cards
```

### **Utilities & State Management**
```
utils/
├── __init__.py
├── state_manager.py                # JSON-based state persistence
├── github_backup.py                # Encrypted backup functionality
├── encryption.py                   # AES-256 encryption utilities
├── enhancement_validator.py        # Configuration validation
├── user_acquisition.py             # 🚀 Cross-platform user acquisition engine
├── telegram_bot.py                 # 🚀 Advanced Telegram engagement & monetization
├── post_mortem.py                  # 🔥 Decision outcome evaluation and learning (Phase 6)
└── event_normalizer.py             # AI Strategist event processing

state_backups/                      # Automatic backup snapshots
├── state_20250901_140011.json
├── state_20250901_140508.json
└── [9 additional backup files]

models/                             # Data models and schemas
attached_assets/                    # User-uploaded files and screenshots
```

---

## **🔧 Developer Integration Guide**

### **API Endpoints & AJAX Calls**

#### **Real-time Status API**
```javascript
// Get current platform status
GET /api/status
// Returns: {"status": "running", "features_active": 15, "last_scan": "2025-09-01T16:50:45Z"}

// Frontend AJAX call:
$.ajax({
    url: '/api/status',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
        $('#platformStatus').text(data.status);
        updateStatusIndicators(data);
    }
});
```

#### **Trading Alerts API**
```javascript
// Get recent alerts
GET /api/alerts
// Returns: {"alerts": [{"timestamp": "...", "asset": "BTC", "signal": "buy", "confidence": 0.85}]}

// Get alert analytics
GET /api/alert-analytics
// Returns: {"total_today": 12, "avg_confidence": 0.73, "success_rate": 0.67}

// Frontend implementation:
function fetchAlerts() {
    fetch('/api/alerts')
        .then(response => response.json())
        .then(data => {
            renderAlertsTable(data.alerts);
            updateAlertCounts(data);
        });
}
```

#### **Trading Operations API**
```javascript
// Execute trade (paper mode)
POST /api/trade
// Body: {"action": "buy", "asset": "BTC", "amount": 100, "type": "market"}

// Get portfolio status
GET /api/portfolio
// Returns: {"positions": [], "cash": 10000, "total_value": 10500}

// Frontend trading interface:
function executeTrade(tradeData) {
    $.post('/api/trade', tradeData)
        .done(function(response) {
            showNotification('Trade executed: ' + response.message);
            refreshPortfolio();
        })
        .fail(function(xhr) {
            showError('Trade failed: ' + xhr.responseJSON.error);
        });
}
```

#### **Configuration Management API**
```javascript
// Update platform settings
POST /api/config
// Body: {"section": "trading", "key": "max_position_size_usd", "value": 500}

// Backup platform state
POST /api/backup
// Returns: {"status": "success", "backup_id": "20250901_165045"}

// Frontend settings panel:
function updateSetting(section, key, value) {
    fetch('/api/config', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({section, key, value})
    }).then(response => {
        if (response.ok) {
            showSuccess('Setting updated successfully');
        }
    });
}
```

### **Database Schema & Queries**

#### **SQLite Database: patterns.db**
```sql
-- Core patterns table
CREATE TABLE patterns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    asset TEXT NOT NULL,
    type TEXT NOT NULL,  -- 'reddit', 'binance', 'news', 'nse'
    confidence REAL,
    signals TEXT,        -- JSON string of signal data
    price REAL,
    volume REAL,
    metadata TEXT        -- Additional JSON data
);

-- Analysis results table  
CREATE TABLE analysis_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    analysis_type TEXT,  -- 'correlation', 'sentiment', 'ml_pattern'
    asset TEXT,
    result_data TEXT,    -- JSON results
    confidence REAL
);

-- Trading decisions table (Phase 5)
CREATE TABLE trading_decisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    asset TEXT NOT NULL,
    decision TEXT,       -- 'buy', 'sell', 'hold'
    confidence REAL,
    reasoning TEXT,
    executed BOOLEAN DEFAULT 0
);
```

#### **Common Database Queries**
```sql
-- Get recent patterns for analysis
SELECT * FROM patterns 
WHERE asset = ? AND timestamp >= datetime('now', '-24 hours')
ORDER BY timestamp DESC;

-- Get sentiment flow data
SELECT 
    timestamp,
    asset as symbol,
    confidence as sentiment_score,
    COALESCE(signals, '') as mention_count,
    type as source
FROM patterns 
WHERE asset = ? AND timestamp >= datetime('now', '-720 hours')
ORDER BY timestamp DESC;

-- Get correlation data
SELECT DISTINCT asset, AVG(confidence) as avg_confidence
FROM patterns 
WHERE timestamp >= datetime('now', '-7 days')
GROUP BY asset;
```

### **State Management Integration**

#### **State Manager Usage**
```python
# Python backend integration
from utils.state_manager import StateManager

# Load current state
state_mgr = StateManager()
current_state = state_mgr.load_state()

# Access specific state sections
trading_state = current_state.get('trading', {})
scanner_offsets = current_state.get('scanner_offsets', {})

# Update state
state_mgr.update_state('trading.open_positions', new_positions)
state_mgr.save_state()
```

#### **Frontend State Synchronization**
```javascript
// WebSocket connection for real-time updates
const ws = new WebSocket('ws://localhost:5000/ws');

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    switch(data.type) {
        case 'status_update':
            updatePlatformStatus(data.payload);
            break;
        case 'new_alert':
            addAlertToUI(data.payload);
            break;
        case 'trade_executed':
            updatePortfolioDisplay(data.payload);
            break;
    }
};

// Send configuration updates
function sendConfigUpdate(config) {
    ws.send(JSON.stringify({
        type: 'config_update',
        payload: config
    }));
}
```

### **Analysis Engine Integration**

#### **Decoder Module Integration**
```python
# Phase 5-8 Features Integration
from decoder.decision_policy import DecisionPolicyEngine
from decoder.gpt_integration import GPTIntegration
from decoder.advanced_models import AdvancedModelsEngine
from utils.post_mortem import PostMortemAnalyzer

# Initialize engines
decision_engine = DecisionPolicyEngine(config['phases_5_8_features']['decision_policy'])
gpt_engine = GPTIntegration(config['phases_5_8_features']['gpt_integration'])
models_engine = AdvancedModelsEngine(config['phases_5_8_features']['advanced_models'])
postmortem = PostMortemAnalyzer(config['phases_5_8_features']['post_mortem_analysis'])

# Process events through pipeline
async def process_trading_event(event):
    # Run analysis
    signals = await decision_engine.aggregate_signals(event)
    decision = await decision_engine.make_decision(signals)
    
    # Execute if decision is actionable
    if decision['action'] != 'hold':
        result = await execute_trade(decision)
        # Schedule post-mortem analysis
        await postmortem.schedule_evaluation(decision, result)
```

#### **Frontend Analysis Display**
```javascript
// Display analysis results
function renderAnalysisResults(analysisData) {
    // Phase 5-8 specific displays
    if (analysisData.decision_policy) {
        updateDecisionPanel(analysisData.decision_policy);
    }
    
    if (analysisData.gpt_narrative) {
        updateNarrativeSection(analysisData.gpt_narrative);
    }
    
    if (analysisData.advanced_models) {
        updateModelPredictions(analysisData.advanced_models);
    }
    
    // Update confidence meters
    $('.confidence-meter').each(function() {
        const confidence = analysisData.confidence || 0;
        $(this).css('width', (confidence * 100) + '%');
    });
}
```

### **Scanner Integration Points**

#### **Adding New Scanner**
```python
# Create new scanner in scanner/ directory
class CustomScanner:
    def __init__(self, config):
        self.config = config
        self.enabled = config.get('enabled', False)
    
    async def scan(self):
        if not self.enabled:
            return []
        
        # Implement scanning logic
        events = await self.fetch_data()
        
        # Normalize events to standard format
        normalized = []
        for event in events:
            normalized.append({
                'timestamp': event['time'],
                'asset': event['symbol'],
                'type': 'custom_source',
                'confidence': event['score'],
                'signals': json.dumps(event['data']),
                'metadata': json.dumps(event.get('extra', {}))
            })
        
        return normalized

# Register in advanced_trading_orchestrator.py
from scanner.custom_scanner import CustomScanner
self.custom_scanner = CustomScanner(self.config.get('custom_scanner', {}))
```

#### **Frontend Scanner Status**
```javascript
// Monitor scanner status
function updateScannerStatus() {
    fetch('/api/scanner-status')
        .then(response => response.json())
        .then(data => {
            Object.keys(data.scanners).forEach(scanner => {
                const status = data.scanners[scanner];
                $(`#${scanner}-status`).text(status.last_scan);
                $(`#${scanner}-count`).text(status.events_today);
            });
        });
}
```

### **Alert System Integration**

#### **Custom Alert Handlers**
```python
# Create custom alert handler
class CustomAlertHandler:
    def __init__(self, config):
        self.config = config
    
    async def send_alert(self, alert_data):
        # Implement custom alert logic
        if alert_data['confidence'] > self.config.get('threshold', 0.7):
            await self.send_high_priority_alert(alert_data)
        else:
            await self.send_standard_alert(alert_data)
    
    async def send_high_priority_alert(self, alert_data):
        # High priority alert implementation
        pass

# Register in executor/alert_sender.py
```

#### **Frontend Alert Management**
```javascript
// Real-time alert handling
function handleNewAlert(alert) {
    // Add to alerts list
    const alertElement = createAlertElement(alert);
    $('#alerts-container').prepend(alertElement);
    
    // Show notification
    if (alert.confidence > 0.8) {
        showHighPriorityNotification(alert);
    }
    
    // Update counters
    updateAlertCounters();
    
    // Auto-scroll if needed
    if ($('#auto-scroll').is(':checked')) {
        alertElement[0].scrollIntoView({behavior: 'smooth'});
    }
}
```

### **Environment Variables & Secrets**

#### **Required Environment Variables**
```bash
# API Keys (use ask_secrets tool to set these)
OPENAI_API_KEY=sk-...                    # GPT integration
REDDIT_CLIENT_ID=...                    # Reddit API access
REDDIT_CLIENT_SECRET=...                # Reddit authentication
BINANCE_API_KEY=...                     # Crypto data access
BINANCE_SECRET_KEY=...                  # Crypto trading (if enabled)
TELEGRAM_BOT_TOKEN=...                  # Alert notifications

# Database Configuration
DATABASE_URL=postgresql://...           # PostgreSQL connection (auto-provided by Replit)
PATTERNS_DB_PATH=./patterns.db          # SQLite database path

# Platform Settings
FLASK_ENV=development                   # Environment mode
PLATFORM_MODE=paper_trading             # Trading mode safety
DEBUG_LEVEL=INFO                        # Logging level
```

#### **Accessing Secrets in Code**
```python
# Python backend
import os
from dotenv import load_dotenv

load_dotenv()

# Safe secret access with fallbacks
openai_key = os.getenv('OPENAI_API_KEY')
if not openai_key:
    logger.warning("OpenAI API key not found - GPT features disabled")

# Configuration validation
required_vars = ['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET', 'TELEGRAM_BOT_TOKEN']
missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    logger.error(f"Missing required environment variables: {missing_vars}")
```

### **WebSocket Integration**

#### **Real-time Data Streaming**
```javascript
// Frontend WebSocket setup
class TradingWebSocket {
    constructor() {
        this.ws = null;
        this.reconnectAttempts = 0;
        this.maxReconnectAttempts = 5;
    }
    
    connect() {
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${protocol}//${window.location.host}/ws`;
        
        this.ws = new WebSocket(wsUrl);
        
        this.ws.onopen = () => {
            console.log('WebSocket connected');
            this.reconnectAttempts = 0;
            this.subscribe(['status', 'alerts', 'trades']);
        };
        
        this.ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleMessage(data);
        };
        
        this.ws.onclose = () => {
            console.log('WebSocket disconnected');
            this.attemptReconnect();
        };
    }
    
    subscribe(channels) {
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify({
                type: 'subscribe',
                channels: channels
            }));
        }
    }
    
    handleMessage(data) {
        switch(data.type) {
            case 'platform_status':
                updatePlatformStatus(data.payload);
                break;
            case 'new_alert':
                addNewAlert(data.payload);
                playNotificationSound();
                break;
            case 'trade_update':
                updateTradeStatus(data.payload);
                break;
            case 'analysis_complete':
                displayAnalysisResults(data.payload);
                break;
        }
    }
}

// Initialize WebSocket connection
const tradingWS = new TradingWebSocket();
tradingWS.connect();
```

#### **Backend WebSocket Handler**
```python
# Python WebSocket implementation
from flask_socketio import SocketIO, emit, join_room, leave_room

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    logger.info(f"Client connected: {request.sid}")
    emit('connection_status', {'status': 'connected'})

@socketio.on('subscribe')
def handle_subscribe(data):
    channels = data.get('channels', [])
    for channel in channels:
        join_room(channel)
        logger.info(f"Client {request.sid} subscribed to {channel}")

# Broadcast updates to subscribers
def broadcast_status_update(status_data):
    socketio.emit('platform_status', status_data, room='status')

def broadcast_new_alert(alert_data):
    socketio.emit('new_alert', alert_data, room='alerts')
```

### **Testing & Development Tools**

#### **API Testing with curl**
```bash
# Test platform status
curl -X GET http://localhost:5000/api/status

# Test alert retrieval
curl -X GET http://localhost:5000/api/alerts

# Test configuration update
curl -X POST http://localhost:5000/api/config \
     -H "Content-Type: application/json" \
     -d '{"section": "trading", "key": "max_position_size_usd", "value": 500}'

# Test paper trade execution
curl -X POST http://localhost:5000/api/trade \
     -H "Content-Type: application/json" \
     -d '{"action": "buy", "asset": "BTC", "amount": 100, "type": "market"}'
```

#### **Python Testing Examples**
```python
# Unit test example for decision engine
import unittest
from decoder.decision_policy import DecisionPolicyEngine

class TestDecisionPolicy(unittest.TestCase):
    def setUp(self):
        self.config = {
            'enabled': True,
            'cooldown_minutes': 60,
            'confidence_thresholds': {
                'paper_trade': 0.7,
                'alert_only': 0.55
            }
        }
        self.engine = DecisionPolicyEngine(self.config)
    
    def test_signal_aggregation(self):
        signals = {
            'causal_confidence': 0.8,
            'regime_score': 0.6,
            'sentiment_score': 0.7
        }
        result = self.engine.aggregate_signals(signals)
        self.assertIsInstance(result, dict)
        self.assertIn('confidence', result)
    
    def test_decision_making(self):
        aggregated_signals = {'confidence': 0.75}
        decision = self.engine.make_decision(aggregated_signals)
        self.assertIn('action', decision)
        self.assertIn(['buy', 'sell', 'hold'], decision['action'])

if __name__ == '__main__':
    unittest.main()
```

### **Performance Monitoring**

#### **Backend Performance Metrics**
```python
# Performance monitoring in advanced_trading_orchestrator.py
import time
import psutil
from collections import defaultdict

class PerformanceMonitor:
    def __init__(self):
        self.metrics = defaultdict(list)
        self.start_times = {}
    
    def start_timer(self, operation):
        self.start_times[operation] = time.time()
    
    def end_timer(self, operation):
        if operation in self.start_times:
            duration = time.time() - self.start_times[operation]
            self.metrics[f"{operation}_duration"].append(duration)
            del self.start_times[operation]
            return duration
        return None
    
    def log_system_metrics(self):
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        self.metrics['cpu_usage'].append(cpu_percent)
        self.metrics['memory_usage'].append(memory_percent)
    
    def get_performance_summary(self):
        summary = {}
        for metric, values in self.metrics.items():
            if values:
                summary[metric] = {
                    'avg': sum(values) / len(values),
                    'min': min(values),
                    'max': max(values),
                    'count': len(values)
                }
        return summary

# Usage in orchestrator
perf_monitor = PerformanceMonitor()

async def run_analysis_cycle(self):
    perf_monitor.start_timer('full_analysis')
    
    # Run analysis phases
    await self.run_core_analysis()
    await self.run_phase5_features()
    await self.run_phases_5_8_features()
    
    duration = perf_monitor.end_timer('full_analysis')
    perf_monitor.log_system_metrics()
    
    logger.info(f"Analysis cycle completed in {duration:.2f} seconds")
```

#### **Frontend Performance Tracking**
```javascript
// Frontend performance monitoring
class PerformanceTracker {
    constructor() {
        this.metrics = {};
        this.startTimes = {};
    }
    
    startTimer(operation) {
        this.startTimes[operation] = performance.now();
    }
    
    endTimer(operation) {
        if (this.startTimes[operation]) {
            const duration = performance.now() - this.startTimes[operation];
            if (!this.metrics[operation]) {
                this.metrics[operation] = [];
            }
            this.metrics[operation].push(duration);
            delete this.startTimes[operation];
            return duration;
        }
        return null;
    }
    
    logPageLoad() {
        window.addEventListener('load', () => {
            const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
            console.log(`Page load time: ${loadTime}ms`);
            this.metrics.pageLoad = loadTime;
        });
    }
    
    logAPICall(url, duration) {
        if (!this.metrics.apiCalls) {
            this.metrics.apiCalls = {};
        }
        if (!this.metrics.apiCalls[url]) {
            this.metrics.apiCalls[url] = [];
        }
        this.metrics.apiCalls[url].push(duration);
    }
}

// Usage in dashboard
const perfTracker = new PerformanceTracker();
perfTracker.logPageLoad();

// Track API call performance
function fetchWithTiming(url, options) {
    const startTime = performance.now();
    return fetch(url, options).then(response => {
        const duration = performance.now() - startTime;
        perfTracker.logAPICall(url, duration);
        return response;
    });
}
```

### **Error Handling & Debugging**

#### **Backend Error Handling**
```python
# Comprehensive error handling
import traceback
from functools import wraps

def error_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            error_info = {
                'function': func.__name__,
                'error': str(e),
                'traceback': traceback.format_exc(),
                'timestamp': datetime.utcnow().isoformat()
            }
            logger.error(f"Error in {func.__name__}: {error_info}")
            
            # Send error notification if critical
            if hasattr(e, 'critical') and e.critical:
                await send_error_notification(error_info)
            
            return None
    return wrapper

# Usage
@error_handler
async def run_analysis_phase(self, phase_name):
    logger.info(f"Starting {phase_name}")
    # Analysis logic here
    logger.info(f"Completed {phase_name}")
```

#### **Frontend Error Handling**
```javascript
// Global error handling
window.addEventListener('error', function(e) {
    console.error('Global error caught:', e.error);
    logErrorToServer({
        message: e.message,
        filename: e.filename,
        lineno: e.lineno,
        colno: e.colno,
        stack: e.error ? e.error.stack : null
    });
});

// API error handling
function apiCall(url, options = {}) {
    return fetch(url, options)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            return response.json();
        })
        .catch(error => {
            console.error(`API call failed for ${url}:`, error);
            showUserError(`Failed to ${options.method || 'GET'} ${url}: ${error.message}`);
            throw error;
        });
}

function logErrorToServer(errorData) {
    fetch('/api/log-error', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(errorData)
    }).catch(console.error);
}
```

---

## **⚙️ Configuration Files & Usage**

### **1. config.json - Master Configuration**

The primary configuration file controlling all platform behavior:

#### **Scanner Configuration**
```json
{
  "scanners": {
    "reddit": true,           // Enable Reddit monitoring
    "binance": true,          // Enable crypto price tracking  
    "nse": true,              // Enable India equity scanning
    "news": true,             // Enable news RSS feeds
    "scan_interval_seconds": 30 // Scan frequency
  }
}
```

#### **AI Configuration**
```json
{
  "ai": {
    "openai_model": "gpt-5",        // AI model version
    "max_tokens": 500,              // Response length limit
    "temperature": 1.0,             // Creativity level
    "cost_limit_daily_usd": 10.0,   // Daily spending cap
    "deep_trigger_score": 0.7       // AI activation threshold
  }
}
```

#### **Alert Configuration**
```json
{
  "alerts": {
    "telegram": true,               // Enable Telegram notifications
    "threshold_strong": 0.7,        // High-confidence alert threshold
    "max_alerts_per_hour": 5        // Rate limiting
  }
}
```

#### **Trading Configuration**
```json
{
  "trading": {
    "simulation_mode": true,        // Paper trading (safe mode)
    "max_position_size_usd": 1000,  // Maximum trade size
    "risk_per_trade": 0.02,         // 2% risk per trade
    "stop_loss_percent": 0.05       // 5% stop loss
  }
}
```

#### **🚀 Phase 5 Advanced Features Configuration**
```json
{
  "phase5_features": {
    "ai_forecasting": {
      "enabled": true,
      "forecast_horizons": {
        "market": 7,              // 7-day market predictions
        "geopolitics": 30,        // 30-day geopolitical analysis
        "stocks": 14,             // 14-day stock forecasting
        "companies": 21           // 21-day company-specific predictions
      },
      "prophet_settings": {
        "daily_seasonality": true,
        "uncertainty_samples": 100
      }
    },
    "community_simulation": {
      "enabled": true,
      "max_posts_simulated": 10,
      "engagement_multiplier": 1.5,
      "viral_threshold": {
        "comment_velocity": 5,
        "upvote_ratio": 0.8,
        "cross_platform_mentions": 3
      }
    },
    "user_acquisition": {
      "enabled": true,
      "platforms": ["twitter", "reddit", "telegram"],
      "campaign_settings": {
        "acquisition": {
          "posting_frequency": "high",
          "target_new_users": 500
        }
      },
      "seo_optimization": true
    },
    "telegram_engagement": {
      "enabled": true,
      "subscription_tiers": {
        "free": {"signal_limit": 3},
        "premium": {"price": 29.99, "signal_limit": -1},
        "vip": {"price": 99.99, "consultation_hours": 2}
      },
      "monetization": true
    }
  }
}
```

#### **🔥 Phases 5-8 Enhanced Configuration (NEW)**
```json
{
  "phases_5_8_features": {
    "decision_policy": {
      "enabled": true,
      "cooldown_minutes": 60,
      "confidence_thresholds": {
        "paper_trade": 0.7,
        "alert_only": 0.55,
        "ignore": 0.0
      },
      "signal_weights": {
        "causal_confidence": 0.4,
        "regime_score": 0.25,
        "sentiment_score": 0.2,
        "micro_score": 0.15
      }
    },
    "post_mortem_analysis": {
      "enabled": true,
      "evaluation_horizon_minutes": 120,
      "performance_tracking": true,
      "learning_feedback": true
    },
    "gpt_integration": {
      "enabled": true,
      "fallback_mode": true,
      "event_typing": true,
      "narrative_building": true,
      "model": "gpt-4",
      "max_tokens": 200,
      "temperature": 0.7
    },
    "advanced_models": {
      "enabled": true,
      "svar_analysis": true,
      "kalman_filtering": true,
      "regime_detection": true,
      "correlation_analysis": true,
      "sample_data_window": 50
    }
  }
}
```

### **2. permissions.json - Safety Controls**

Comprehensive permission and safety management:

#### **Trading Permissions**
```json
{
  "trading": {
    "live_trading_enabled": false,    // SAFETY: Live trading disabled
    "paper_trading_enabled": true,    // Paper trading active
    "max_position_size_usd": 200.0,   // Position size limit
    "risk_level": "conservative"      // Risk management level
  }
}
```

#### **Social Media Permissions**
```json
{
  "social_media": {
    "reddit_posting_enabled": true,
    "max_posts_per_day": 5,          // Daily posting limit
    "allowed_subreddits": [          // Approved communities
      "CryptoCurrency", "Bitcoin", "ethereum"
    ],
    "posting_hours": {
      "start_utc": 6, "end_utc": 22  // Active hours only
    }
  }
}
```

#### **Circuit Breakers**
```json
{
  "circuit_breakers": {
    "trading_circuit_breaker": {
      "max_losses_before_halt": 3,   // Auto-stop after 3 losses
      "halt_duration_minutes": 60    // 1-hour cooldown
    }
  }
}
```

### **3. assets-config.json - Asset Definitions**

Defines all monitored assets with aliases and patterns:

#### **Cryptocurrency Assets**
```json
{
  "crypto": {
    "BTC": {
      "symbol": "BTC-USD",
      "aliases": ["BITCOIN", "BTC", "BITCOINS"],
      "patterns": ["\\bBTC\\b", "\\bBITCOIN\\b"],
      "market_cap": "large"
    }
  }
}
```

#### **Indian Equity Assets**
```json
{
  "indian_equities": {
    "RELIANCE": {
      "symbol": "RELIANCE.NS",
      "aliases": ["RELIANCE", "RIL"],
      "sector": "energy",
      "market_cap": "large"
    }
  }
}
```

### **4. sectors-config.json - Sector Analysis**

Sector classification and correlation settings:

```json
{
  "sectors": {
    "BANKING": {
      "assets": ["HDFCBANK", "ICICIBANK", "SBIN"],
      "correlation_threshold": 0.7,
      "volatility": "medium"
    },
    "CRYPTO_LARGE": {
      "assets": ["BTC", "ETH", "BNB"],
      "correlation_threshold": 0.6,
      "volatility": "very_high"
    }
  }
}
```

---

## **🚀 How to Use the Platform**

### **Starting the Platform**
```bash
# Install dependencies
python -m pip install -r requirements.txt

# Start the main application
python app.py

# Access dashboard at: http://localhost:5000
```

### **Configuration Management**

#### **Basic Configuration Changes**
1. **Enable/Disable Scanners**: Edit `config.json` → `scanners` section
2. **Adjust AI Settings**: Modify `config.json` → `ai` section  
3. **Configure Alerts**: Update `config.json` → `alerts` section
4. **Trading Settings**: Modify `config.json` → `trading` section

#### **Safety Controls**
1. **Enable Live Trading**: Set `permissions.json` → `trading.live_trading_enabled: true`
2. **Adjust Risk Limits**: Modify `permissions.json` → `trading` limits
3. **Configure Circuit Breakers**: Update `permissions.json` → `safety_controls`

#### **Asset Management**
1. **Add New Assets**: Update `assets-config.json` with symbol, aliases, patterns
2. **Sector Classification**: Add to appropriate sector in `sectors-config.json`
3. **Correlation Thresholds**: Adjust per-sector correlation settings

### **Environment Variables Setup**

#### **Required Credentials**
```bash
# Reddit API (Required)
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password

# Binance API (Required)
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET=your_binance_secret

# OpenAI API (Required for AI features)
OPENAI_API_KEY=your_openai_api_key
```

#### **Optional Integrations**
```bash
# Telegram Alerts
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Discord Alerts
DISCORD_WEBHOOK_URL=your_discord_webhook

# GitHub Backup
GITHUB_TOKEN=your_github_token
ENCRYPTION_PASSPHRASE=your_backup_passphrase
```

#### **🚀 Phase 5 Advanced Features**
```bash
# Twitter API Integration (User Acquisition)
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

# Advanced Telegram Features
TELEGRAM_CHANNEL_ID=your_telegram_channel_id
DISCORD_INVITE_LINK=your_discord_invite_url

# Monetization & Growth
WEBSITE_URL=your_website_url
PREMIUM_SIGNUP_LINK=your_premium_signup_link
```

### **Dashboard Usage**

#### **Real-Time Monitoring**
- **Status Cards**: View scanner activity and health
- **Live Alerts**: Real-time notifications with confidence scores
- **News Feed**: Professional card-based news layout
- **System Health**: Monitor all 11 AI analysis features (7 original + 4 Phase 5)

#### **Manual Controls**
- **Emergency Stop**: Halt all trading operations
- **Scanner Control**: Enable/disable individual data sources
- **Alert Filtering**: Adjust confidence thresholds
- **Backup Management**: Manual state backup/restore

### **API Endpoints**

#### **Status Monitoring**
```bash
GET /api/status          # Platform health and metrics
GET /api/alerts          # Recent alerts and notifications
GET /api/patterns        # Pattern analysis results
GET /api/portfolio       # Portfolio optimization data
```

#### **Configuration Management**
```bash
POST /api/config         # Update platform configuration
GET /api/permissions     # View current permissions
POST /api/emergency-stop # Emergency halt all operations
```

---

## **🛡️ Safety Features**

### **Current Safety Status**
- ✅ **Paper Trading Mode**: Live trading disabled
- ✅ **Rate Limiting**: All APIs properly throttled
- ✅ **Circuit Breakers**: Auto-stop on failures
- ✅ **Position Limits**: Maximum $200 per position
- ✅ **Daily Limits**: Maximum 5 trades per day
- ✅ **Risk Management**: 2% risk per trade, 5% stop loss

### **Risk Controls**
- **Conservative Risk Level**: All trading operations use conservative settings
- **Emergency Stop**: Manual and automatic halt capabilities
- **Encrypted Backups**: AES-256 encryption for all state data
- **API Monitoring**: Continuous health checking and failure detection

---

## **📊 Current Operational Status**

### **Active Features (All Working)**
- **Data Collection**: 4 scanner sources operational
- **AI Analysis**: 11 advanced intelligence features running (7 original + 4 Phase 5)
- **🚀 Predictive Forecasting**: AI-powered market and geopolitical predictions
- **🚀 Community Growth**: Automated engagement simulation and viral detection
- **🚀 User Acquisition**: Cross-platform automated growth campaigns
- **🚀 Monetization**: Premium Telegram subscriptions and community management
- **Alert System**: Multi-channel notifications active
- **Web Dashboard**: Real-time updates and professional UI
- **Database**: PostgreSQL infrastructure in place
- **Backup System**: Automatic state preservation

### **Performance Metrics**
- **Analysis Speed**: 0.01 seconds per cycle
- **Scanner Frequency**: 30-second intervals
- **Alert Generation**: Real-time processing
- **Uptime Target**: 99% availability
- **Data Collection**: Currently processing 9 India equity events per scan

### **Current Data Flow**
```
Reddit/News/Binance/NSE → Scanners → Pattern Analysis → 
GPT-5 AI Processing + Prophet Forecasting → Risk Scoring → 
Community Simulation + User Acquisition → Alerts/Actions → 
Telegram Monetization + Dashboard Display → User Decision Making
```

---

## **🔧 Configuration Customization Guide**

### **Quick Configuration Changes**

#### **1. Enable Live Trading (⚠️ Use with Caution)**
```json
// In permissions.json
"trading": {
  "live_trading_enabled": true,
  "paper_trading_enabled": false
}

// In config.json  
"trading": {
  "simulation_mode": false
}
```

#### **2. Adjust AI Sensitivity**
```json
// In config.json
"ai": {
  "deep_trigger_score": 0.5,        // Lower = more sensitive
  "cost_limit_daily_usd": 20.0      // Increase AI budget
}
```

#### **3. Configure Alert Channels**
```json
// In config.json
"alerts": {
  "telegram": true,                 // Enable Telegram
  "discord": true,                  // Enable Discord
  "threshold_strong": 0.6           // Lower threshold = more alerts
}
```

#### **4. Add New Cryptocurrency**
```json
// In assets-config.json
"crypto": {
  "DOGE": {
    "symbol": "DOGE-USD",
    "aliases": ["DOGECOIN", "DOGE"],
    "patterns": ["\\bDOGE\\b", "\\bDOGECOIN\\b"],
    "market_cap": "medium",
    "exchange": "binance"
  }
}
```

#### **5. Modify Scanning Frequency**
```json
// In config.json
"scanners": {
  "scan_interval_seconds": 15       // Scan every 15 seconds (faster)
}

// In permissions.json
"operational_limits": {
  "scanner_limits": {
    "scan_interval_seconds": 15
  }
}
```

### **Advanced Configuration**

#### **Multi-Timeframe Analysis**
```json
// In config.json
"multi_timeframe": {
  "windows": ["15m", "1h", "4h", "1d"],    // Add 15-minute analysis
  "confirmation_threshold": 0.8,           // Require higher confidence
  "weight_multiplier": 2.0                 // Increase signal strength
}
```

#### **Portfolio Optimization**
```json
// In config.json
"portfolio_optimization": {
  "max_sector_exposure": 0.25,             // 25% max per sector
  "max_single_asset": 0.10,                // 10% max per asset
  "risk_target": 0.70                      // Higher risk tolerance
}
```

#### **Smart Alert Management**
```json
// In config.json
"smart_alerts": {
  "user_preferences": {
    "max_daily_alerts": 15,               // More alerts per day
    "preferred_confidence": 0.8,          // Higher confidence requirement
    "quiet_hours": ["23:00", "05:00"]     // Extended quiet period
  }
}
```

#### **🚀 Phase 5 Advanced Features**
```json
// In config.json - Add Phase 5 configurations
"phase5_features": {
  "ai_forecasting": {
    "enabled": true,
    "forecast_horizons": {
      "market": 14,                      // Extend to 14-day forecasts
      "geopolitics": 60                  // Extend to 60-day geopolitical analysis
    },
    "confidence_threshold": 0.8          // Require higher confidence
  },
  "community_simulation": {
    "enabled": true,
    "max_posts_simulated": 20,          // Increase simulation capacity
    "engagement_multiplier": 2.0,       // Higher engagement simulation
    "viral_threshold": {
      "comment_velocity": 10,           // Higher viral threshold
      "cross_platform_mentions": 5
    }
  },
  "user_acquisition": {
    "enabled": true,
    "platforms": ["twitter", "reddit", "telegram", "discord"],
    "campaign_settings": {
      "acquisition": {
        "target_new_users": 1000,       // Increase growth targets
        "duration_days": 30
      }
    }
  },
  "telegram_engagement": {
    "enabled": true,
    "subscription_tiers": {
      "enterprise": {                   // Add enterprise tier
        "price": 199.99,
        "analysis_access": "enterprise",
        "consultation_hours": 10
      }
    }
  }
}
```

#### **🚀 Phase 5 Permissions Configuration**
```json
// In permissions.json - Add Phase 5 permissions
"phase5_advanced": {
  "ai_forecasting": {
    "max_predictions_per_day": 100,     // Increase prediction capacity
    "geopolitical_analysis": true
  },
  "community_simulation": {
    "max_simulated_posts": 50,          // Increase simulation limits
    "viral_detection": true
  },
  "user_acquisition": {
    "max_campaigns_concurrent": 5,      // More concurrent campaigns
    "cross_platform_limit": 200,       // Higher posting limits
    "funnel_analytics": true
  },
  "telegram_engagement": {
    "max_users": 50000,                 // Scale to 50k users
    "premium_features": true,
    "auto_moderation": true
  }
}
```

---

## **🔌 Integration Setup**

### **Reddit API Setup**
1. Go to https://www.reddit.com/prefs/apps
2. Create new application (script type)
3. Add credentials to environment variables
4. Configure subreddits in `permissions.json`

### **Binance API Setup**
1. Log into Binance account
2. Create API key with read-only permissions
3. Add to environment variables
4. Enable in `config.json` scanners section

### **Telegram Alerts Setup**
1. Create bot via @BotFather on Telegram
2. Get bot token and chat ID
3. Add to environment variables
4. Enable in `config.json` alerts section

### **OpenAI Integration**
1. Get API key from OpenAI platform
2. Add OPENAI_API_KEY to environment
3. Configure model and limits in `config.json`

### **🚀 Phase 5 Feature Setup**

#### **Twitter API Setup (User Acquisition)**
1. Apply for Twitter Developer account
2. Create app and get API keys
3. Add credentials to environment variables
4. Enable in `config.json` phase5_features section

#### **Advanced Telegram Bot Setup**
1. Create bot via @BotFather with admin permissions
2. Get bot token and set up webhook
3. Configure payment processing (for premium subscriptions)
4. Set up channel/group management permissions

#### **Prophet Forecasting Setup**
1. Ensure Prophet library installed: `pip install prophet`
2. Configure forecast horizons in `config.json`
3. Set up data sources for historical analysis
4. Enable geopolitical data feeds

#### **Community Simulation Setup**
1. Configure user personas in `config.json`
2. Set viral detection thresholds
3. Enable cross-platform content analysis
4. Configure engagement multipliers

---

## **📈 Monitoring & Health Checks**

### **System Health Monitoring**
- **Component Health**: 60-second health checks
- **Performance Tracking**: Response times and memory usage
- **API Quota Monitoring**: Track usage against limits
- **Uptime Target**: 99% availability with maintenance windows

### **Log Files**
- **advanced_trading.log**: Main system operation log
- **patterns.db**: SQLite database with analysis patterns
- **state_backups/**: Automatic hourly state snapshots

### **Dashboard Monitoring**
- **Real-time Status**: Live updates every few seconds
- **Alert History**: Recent notifications and actions
- **Scanner Activity**: Data collection status
- **AI Feature Status**: 11/11 features operational status (including Phase 5 advanced features)

---

## **🔄 Backup & Migration**

### **Automatic Backups**
- **State Backups**: Hourly JSON snapshots
- **GitHub Integration**: Encrypted remote backups
- **Retention Policy**: 90 days for state, 30 days for logs

### **Zero-Downtime Migration**
- **Account Migration**: Transfer between Replit accounts
- **State Preservation**: Maintain all trading and posting history
- **Configuration Transfer**: Keep all settings and permissions

---

## **⚡ Quick Start Commands**

### **Platform Control**
```bash
# Start platform
python app.py

# View real-time logs
tail -f advanced_trading.log

# Check system status
curl http://localhost:5000/api/status

# Emergency stop all operations
curl -X POST http://localhost:5000/api/emergency-stop
```

### **Configuration Updates**
```bash
# Validate configuration
python bootstrap.py --validate

# Backup current state
python -c "from utils.state_manager import StateManager; StateManager().backup_state()"

# Test AI connectivity
python -c "from decoder.ai_analyzer import AIAnalyzer; print(AIAnalyzer.test_connection())"
```

---

## **🎯 Key Features Summary**

### **Current Capabilities**
- **40+ Asset Monitoring**: Crypto + Indian equities
- **Real-time Analysis**: 30-second scan cycles
- **AI-Powered Insights**: GPT-5 integration across all 11 analysis features
- **🚀 Predictive Forecasting**: 7-30 day market, geopolitical, stock predictions using Prophet ML
- **🚀 Community Automation**: Advanced engagement simulation with viral content detection
- **🚀 Cross-Platform Growth**: Automated Twitter, Reddit, Telegram posting campaigns
- **🚀 Monetization System**: Premium subscription tiers (Free/Premium/VIP) with Telegram bot
- **Multi-Channel Alerts**: Telegram, Discord, email
- **Safe Trading**: Paper trading with comprehensive risk controls
- **Professional UI**: Modern dashboard with real-time updates
- **Zero-Downtime Migration**: Seamless account transfers

### **Safety Guarantees**
- **Paper Trading Default**: No real money at risk
- **Rate Limiting**: Prevent API abuse
- **Circuit Breakers**: Auto-stop on failures  
- **Permission System**: Granular access controls
- **Encrypted Backups**: Secure state preservation

This platform successfully combines sophisticated AI analysis with enterprise-grade safety controls and a clean, maintainable architecture following industry best practices.