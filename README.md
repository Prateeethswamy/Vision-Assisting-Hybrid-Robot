# Vision-Assisting-Hybrid-Robot
Vision-Assisting Hybrid Robot
🛡 Hybrid Surveillance & Disaster Response Platform

Team Aurorabots | HAL-42 | Hack-A-League 4.0

**Overview**
The Vision-Assisting Hybrid Robot is an intelligent ground reconnaissance system engineered for:
 Military Surveillance in GPS-denied zones
 Disaster Management & Post-Event Search Operations
🌫 Low-Visibility & Debris-Filled Environments

It combines multi-sensor fusion, real-time telemetry, and hybrid mobility to deliver rapid situational awareness without risking human lives.

**Core Features**
 Multi-Sensor Fusion System
HB100 Doppler Radar for motion detection
Ultrasonic sensors for real-time 2D obstacle mapping
ESP32-CAM for live wireless video streaming
Servo-based directional scanning
Priority-based sensor scheduling

**Hybrid Mobility**
Leg–Wheel Hybrid Mechanism
Adaptable to:
Rubble
Rocky Terrain
Smooth Surfaces
Indoor & Outdoor Environments

**Real-Time Dashboard**
Wireless telemetry
Low-latency monitoring
Live motion alerts
2D obstacle visualization

**Hardware Stack**
ESP32 (Main Controller)
arduino Nano(For wireless control of the hexapod robot using an antenna-based communication system.)
ESP32-CAM (Vision Streaming)
HB100 Doppler Radar Module
Ultrasonic Sensors (2D Mapping)
Servo Motors (Directional Scan)
Hybrid Leg-Wheel Drive System

**Software Stack**
Embedded C / Arduino IDE
Python-based Monitoring Dashboard
Wireless Wi-Fi Communication
Edge-based Processing

**Problem Statement**
Military and disaster-response teams often operate in:
GPS-denied zones
Smoke-filled / low-visibility areas
Structurally unstable environments
This delays intelligence gathering and increases operational risk.

**Our Solution**
A controller-based hybrid robot that:
Detects motion using Doppler radar

Streams live video wirelessly
Generates 2D obstacle maps
Adapts to uneven terrain
Operates reliably in low-visibility conditions
All powered by an energy-efficient embedded edge system
