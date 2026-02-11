# 2-D Point Mass GNC Simulation (Python + PID + Kalman)

## Overview

This project implements a complete Guidance, Navigation, and Control (GNC) Simulation for a planar point mass system in Python.

This system includes:

* Discrete time point mass dynamics
* PID feedback control
* Actuator saturation modeling
* Disturbance injection
* Discrete Kalman filter state estimation
* Structured trade studies evaluating robustness and sensitivity

The goal of this project was to design, simulate, and evaluate a closed loop architecture under realistic noise, disturbance, and implementation constraints.

## System Architecture

This system consists of:

* Plant: 2-D translational point mass dynamics
* Controller: PID feedback controller
* Estimator: Discrete Kalman filter
* Sensors: Noisy position and velocity measurements
* Actuators: Saturated acceleration commands

Block diagram available in /docs/Block Diagram.png

## Trade Studies Conducted

* Disturbance profile sensitivity
* Measurement noise sensitivity
* Process noise (Q) sensitivity
* Sampling rate sensitivity
* Actuator saturation limits

## Key takeaways

* Closed-loop system remains stable under multiple disturbance types
* Measurement noise primarily increases estimation RMSE
* Process noise tuning (Q) trades responsiveness for smoothness
* Actuator limits strongly influence overshoot
* Very slow sampling rates degrade performance

# Purpose

This project demonstrates:

* Classical feedback control design
* State estimation using Kalman filtering
* Noise and disturbance modeling
* Modular simulation architecture
* Structured engineering trade studies