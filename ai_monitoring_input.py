"""
Project: AI IT Infrastructure Monitoring Assistant - Input Processor

The objective is to receive infrastructure metrics, validate their basic types, calculate average utilization and prepare information for an AI model.

"""

# Ai Infrastructure monitoring assisitant

# 1. Application configuration

app_name= " AI Infrastructure Monitor"
model_name= "gpt-40-mini"

# 2. Infrastructure metrics( simnulated API data)

server_name= "CITRIX-SERVER-01"
cpu_usage= "95"
memory_usage= "88"
response_time=  "4.5"

# 3. convert incoming string value

cpu_usage= int(cpu_usage)
memory_usage=int(memory_usage)
response_time=float(response_time)

# 4. calculate avarage utilization 

avg_utilization= (cpu_usage+memory_usage)/2

# 5. determine infrasture health

is_critical= cpu_usage>=90 or memory_usage>=90

# 6. Handle optional information 

assigned_engineer= None

# 7. Prepare information for AI Model

monitoring_data ={

    "server": server_name,
    "cpu_usage": cpu_usage,
    "memory_usage": memory_usage,
    "response_time": response_time,
    "avg_utilisation": avg_utilization,
    "is_critical": is_critical
}

# 8: Display results

print("Application: ", app_name)
print("AI Model: ", model_name)
print("monitoring data: ", monitoring_data)

if is_critical:
    print("Alert : Infrastructure require attention")
else:
    print("Infrasture is Healthy.")

if assigned_engineer is None:
    print(" No engineer is assigned yet.")