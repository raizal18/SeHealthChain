JWT secuirity dependecy
pip install fastapi
pip install "python-jose[cryptography]" "passlib[bcrypt]" python-multipart
pip install pydantic

to run client api run 
1.run server.py in a new terminal in environment
2.run client.py in a new environment
3.go to http://localhost:{port mention for client }/docs <<-- write the port number 


to get simulation

run "run_simulation.py" in new terminal

# Scalable eHealthChain (SeHealthChain)

## Overview
Scalable eHealthChain (SeHealthChain) is a proposed blockchain system designed to address the limitations of traditional blockchain technology in high-throughput, low-latency applications, particularly in the healthcare industry. This system combines reputation-based mechanisms with a sharding scheme to enhance scalability and security, making it suitable for applications such as COVID-19 image transmission.

## Motivation
Traditional blockchain systems face scalability challenges, especially when dealing with large datasets such as medical imaging data. Furthermore, existing solutions for healthcare records management often lack complete decentralization and interoperability with blockchain. SeHealthChain aims to overcome these limitations by introducing a reputation-based scalable blockchain system with a sharding scheme.

## Features
- **Reputation-based Scalability**: SeHealthChain incorporates reputation scores to handle the heterogeneity among evaluators and to establish a basis for reward strategies, thereby enhancing scalability.
- **Sharding Scheme**: The system utilizes a sharding scheme to partition the blockchain into smaller, more manageable segments, improving throughput and latency for high-demand applications.
- **Dual-chain Structure**: SeHealthChain introduces a novel dual-chain structure consisting of TChain and RChain, each serving different purposes to ensure security and high throughput.
- **Enhanced Security**: By utilizing a synchronous Byzantine Fault Tolerance Consensus (BFTC) mechanism for RChain and implementing a modified reputation-based sharding technique, SeHealthChain enhances security levels against attacks.
- **Application in Healthcare**: SeHealthChain is specifically tailored for healthcare applications, offering benefits such as secure transmission of medical records, including COVID-19 images, with low latency.

## Usage
To deploy SeHealthChain and utilize its capabilities, follow these steps:
1. **Install Dependencies**: Ensure that all required dependencies, including Python libraries and blockchain components, are installed.
2. **Configure Reputation Parameters**: Adjust reputation-based parameters according to the specific requirements and characteristics of the healthcare application.
3. **Deploy the System**: Deploy SeHealthChain on a suitable network infrastructure, considering factors such as node distribution and network topology.
4. **Interact with the System**: Utilize the provided APIs or interfaces to interact with SeHealthChain, such as adding new data, retrieving medical records, or transmitting images securely.

## Implementation Details
- **Blockchain Framework**: SeHealthChain is built upon a Python-based blockchain framework, leveraging existing modules and libraries for core functionalities.
- **API Integration**: SeHealthChain provides RESTful APIs for seamless integration with existing healthcare systems or applications.
- **Documentation**: Comprehensive documentation detailing system architecture, deployment instructions, and API usage is provided for developers and users.

## Future Enhancements
- Integration with Healthcare Systems: Seamlessly integrate SeHealthChain with existing electronic health record (EHR) systems and medical imaging platforms.
- Performance Optimization: Continuously optimize SeHealthChain's performance to further enhance scalability and reduce latency, ensuring real-time data transmission for critical healthcare applications.
- Interoperability Standards: Develop interoperability standards to facilitate seamless data exchange between SeHealthChain and other healthcare blockchain systems or networks.


