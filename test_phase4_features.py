#!/usr/bin/env python3
"""
Test Phase 4 Action Layer & User Features
"""

import asyncio
import logging
from executor.trade_executor import TradeExecutor
from executor.alert_sender import AlertSender
from executor.reddit_poster import RedditPoster

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_copy_trading():
    """Test copy trading functionality"""
    logger.info("Testing copy trading functionality...")
    
    executor = TradeExecutor()
    
    # Mock leader trade
    leader_trade = {
        'id': 'leader_trade_123',
        'symbol': 'BTC/USDT',
        'direction': 'long',
        'size': 100.0,
        'entry_price': 50000.0,
        'stop_loss': 49000.0,
        'take_profit': 52000.0,
        'pattern_id': 'pattern_456',
        'score': 85.0
    }
    
    # Test copy trade with 50% risk factor
    result = await executor.copy_trade(leader_trade, 0.5)
    logger.info(f"Copy trade result: {result}")
    
    return result.get('success', False)

async def test_community_alerts():
    """Test community alert broadcasting"""
    logger.info("Testing community alert functionality...")
    
    alert_sender = AlertSender()
    
    # Mock alert content
    alert_content = {
        'webhook': {
            'asset': 'BTC',
            'pattern_type': 'price_movement',
            'source': 'binance',
            'signals': {'price_change_percent': 5.2}
        },
        'discord': {
            'embeds': [{
                'title': 'BTC Alert',
                'description': 'Price movement detected'
            }]
        }
    }
    
    # Test community broadcast
    result = await alert_sender.broadcast_to_community(alert_content, 'reddit')
    logger.info(f"Community broadcast result: {result}")
    
    await alert_sender.cleanup()
    return True

async def test_strategy_sharing():
    """Test strategy sharing functionality"""
    logger.info("Testing strategy sharing functionality...")
    
    poster = RedditPoster()
    
    # Mock strategy
    strategy = {
        'name': 'Momentum Scalping Strategy',
        'description': 'Short-term momentum based on volume and price action',
        'entry_rules': 'Volume spike > 2x normal + price breakout',
        'exit_rules': 'Take profit at 2% or stop loss at 1%',
        'risk_level': 'medium',
        'backtest_performance': '15% annual return, 35% win rate'
    }
    
    # Test strategy sharing
    result = await poster.share_strategy(strategy, 'CryptoCurrency')
    logger.info(f"Strategy sharing result: {result}")
    
    return result

async def test_enhanced_personas():
    """Test enhanced personas"""
    logger.info("Testing enhanced personas...")
    
    poster = RedditPoster()
    
    # Check if collaborative persona exists
    collaborative_persona = None
    for persona in poster.personas:
        if persona['name'] == 'collaborative':
            collaborative_persona = persona
            break
    
    if collaborative_persona:
        logger.info(f"Collaborative persona found: {collaborative_persona}")
        return True
    else:
        logger.error("Collaborative persona not found")
        return False

async def main():
    """Run all Phase 4 tests"""
    logger.info("🚀 Starting Phase 4 feature tests...")
    
    results = {}
    
    try:
        # Test copy trading
        results['copy_trading'] = await test_copy_trading()
        
        # Test community alerts
        results['community_alerts'] = await test_community_alerts()
        
        # Test strategy sharing
        results['strategy_sharing'] = await test_strategy_sharing()
        
        # Test enhanced personas
        results['enhanced_personas'] = await test_enhanced_personas()
        
    except Exception as e:
        logger.error(f"Error during testing: {e}")
        results['error'] = str(e)
    
    # Summary
    logger.info("📊 Phase 4 Test Results:")
    for feature, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        logger.info(f"  {feature}: {status}")
    
    passed = sum(1 for success in results.values() if success)
    total = len(results)
    logger.info(f"Overall: {passed}/{total} tests passed")
    
    return results

if __name__ == "__main__":
    asyncio.run(main())